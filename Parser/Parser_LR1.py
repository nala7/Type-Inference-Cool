from cmp.pycompiler import Item
from cmp.utils import ContainerSet
from cmp.automata import State, multiline_formatter
from Parser.Firsts_Follows import compute_firsts, compute_local_first

import Parser.Parsers_ShiftReduce as ParserSR
from Parser.Automata_Utils import PrintAutomaton


class LR1Parser(ParserSR.ShiftReduceParser):
    def _build_parsing_table(self):
        G = self.G.AugmentedGrammar(True)

        automaton = Build_Automaton_LR1(G)
        for i, node in enumerate(automaton):
            if self.verbose:
                print(i, "\t", "\n\t ".join(str(x) for x in node.state), "\n")
            node.idx = i

        for node in automaton:
            idx = node.idx
            for item in node.state:
                # Your code here!!!
                # - Fill `self.Action` and `self.Goto` according to `item`)
                # - Feel free to use `self._register(...)`)
                if item.IsReduceItem:
                    if item.production.Left == G.startSymbol:
                        key = (idx, G.EOF.Name)
                        value = (self.OK, None)
                        self.conflict |= self._register(self.action, key, value)
                    else:
                        for lookahead in item.lookaheads:
                            key = (idx, lookahead.Name)
                            value = (self.REDUCE, item.production)
                            self.conflict |= self._register(self.action, key, value)
                else:
                    if item.NextSymbol.IsTerminal:
                        key = (idx, item.NextSymbol.Name)
                        value = (
                            self.SHIFT,
                            node.transitions[item.NextSymbol.Name][0].idx,
                        )
                        self.conflict |= self._register(self.action, key, value)
                    else:
                        key = (idx, item.NextSymbol.Name)
                        value = node.transitions[item.NextSymbol.Name][0].idx
                        self.conflict |= self._register(self.goto, key, value)

    @staticmethod
    def _register(table, key, value):
        conflict = False
        if key in table and not table[key] == value:
            #'Shift-Reduce or Reduce-Reduce conflict!!!'
            conflict = True
        table[key] = value
        return conflict


def expand(item, firsts):
    next_symbol = item.NextSymbol
    if next_symbol is None or not next_symbol.IsNonTerminal:
        return []

    lookaheads = ContainerSet()
    # Your code here!!! (Compute lookahead for child items)
    for preview in item.Preview():
        lookaheads.hard_update(compute_local_first(firsts, preview))

    assert not lookaheads.contains_epsilon
    # Your code here!!! (Build and return child items)
    return [Item(prod, 0, lookaheads) for prod in next_symbol.productions]


def compress(items):
    centers = {}

    for item in items:
        center = item.Center()
        try:
            lookaheads = centers[center]
        except KeyError:
            centers[center] = lookaheads = set()
        lookaheads.update(item.lookaheads)

    return {
        Item(x.production, x.pos, set(lookahead)) for x, lookahead in centers.items()
    }


def closure_lr1(items, firsts):
    closure = ContainerSet(*items)

    changed = True
    while changed:
        changed = False

        new_items = ContainerSet()
        # Your code here!!!
        for item in closure:
            expand_set = expand(item, firsts)
            new_items.extend(expand_set)

        changed = closure.update(new_items)

    return compress(closure)


def goto_lr1(items, symbol, firsts=None, just_kernel=False):
    assert (
        just_kernel or firsts is not None
    ), "`firsts` must be provided if `just_kernel=False`"
    items = frozenset(item.NextItem() for item in items if item.NextSymbol == symbol)
    return items if just_kernel else closure_lr1(items, firsts)


def Build_Automaton_LR1(G):
    assert len(G.startSymbol.productions) == 1, "Grammar must be augmented"

    firsts = compute_firsts(G)
    firsts[G.EOF] = ContainerSet(G.EOF)

    start_production = G.startSymbol.productions[0]
    start_item = Item(start_production, 0, lookaheads=(G.EOF,))
    start = frozenset([start_item])

    closure = closure_lr1(start, firsts)
    automaton = State(frozenset(closure), True)

    pending = [start]
    visited = {start: automaton}

    while pending:
        current = pending.pop()
        current_state = visited[current]

        for symbol in G.terminals + G.nonTerminals:
            # Your code here!!! (Get/Build `next_state`)
            closure = closure_lr1(current, firsts)
            goto = goto_lr1(closure, symbol, firsts, True)
            if not goto:
                continue
            try:
                next_state = visited[goto]
            except KeyError:
                closure = closure_lr1(goto, firsts)
                next_state = visited[goto] = State(frozenset(closure), True)
                pending.append(goto)

            current_state.add_transition(symbol.Name, next_state)

    automaton.set_formatter(multiline_formatter)
    return automaton


def Print_Automaton_LR1(automaton):
    PrintAutomaton(automaton, "AutomataLR1.png", "Automata LR(1)")
