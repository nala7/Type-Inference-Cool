import pydot
# from pandas import DataFrame
from PIL import Image
# import streamlit as st
from cmp.automata import State, multiline_formatter
from cmp.utils import ContainerSet


class NFA:
    def __init__(self, states, finals, transitions, start=0):
        self.states = states
        self.start = start
        self.finals = set(finals)
        self.map = transitions
        self.vocabulary = set()
        self.transitions = {state: {} for state in range(states)}

        for (origin, symbol), destinations in transitions.items():
            assert hasattr(destinations, "__iter__"), "Invalid collection of states"
            self.transitions[origin][symbol] = destinations
            self.vocabulary.add(symbol)

        self.vocabulary.discard("")

    def epsilon_transitions(self, state):
        assert state in self.transitions, "Invalid state"
        try:
            return self.transitions[state][""]
        except KeyError:
            return ()

    def graph(self):
        G = pydot.Dot(rankdir="LR", margin=0.1)
        G.add_node(pydot.Node("start", shape="plaintext", label="", width=0, height=0))

        for (start, tran), destinations in self.map.items():
            tran = "ε" if tran == "" else tran
            G.add_node(
                pydot.Node(
                    start, shape="circle", style="bold" if start in self.finals else ""
                )
            )
            for end in destinations:
                G.add_node(
                    pydot.Node(
                        end, shape="circle", style="bold" if end in self.finals else ""
                    )
                )
                G.add_edge(pydot.Edge(start, end, label=tran, labeldistance=2))

        G.add_edge(pydot.Edge("start", self.start, label="", style="dashed"))
        return G

    def _repr_svg_(self):
        #         try:
        return self.graph().create_svg().decode("utf8")


#         except:
#             pass


class DFA(NFA):
    def __init__(self, states, finals, transitions, start=0):
        assert all(isinstance(value, int) for value in transitions.values())
        assert all(len(symbol) > 0 for origin, symbol in transitions)

        transitions = {key: [value] for key, value in transitions.items()}
        NFA.__init__(self, states, finals, transitions, start)
        self.current = start

    def _move(self, symbol):
        try:
            self.current = self.transitions[self.current][symbol][0]
            return True
        except:
            return False

    def _reset(self):
        self.current = self.start

    def recognize(self, string):
        for c in string:
            if not self._move(c):
                return False
        value = self.current in self.finals
        self.current = self.start
        return value




def move(automaton, states, symbol):
    moves = set()
    for state in states:
        try:
            for elem in automaton.transitions[state][symbol]:
                moves.add(elem)
        except KeyError:
            continue
    return moves


def epsilon_closure(automaton, states):
    pending = [s for s in states]  # equivalente a list(states) pero me gusta así :p
    closure = {s for s in states}  # equivalente a  set(states) pero me gusta así :p

    while pending:
        state = pending.pop()
        try:
            for elem in automaton.transitions[state][""]:
                closure.add(elem)
                pending.append(elem)
        except KeyError:
            continue

    return ContainerSet(*closure)


def nfa_to_dfa(automaton):
    transitions = {}

    start = epsilon_closure(automaton, [automaton.start])
    start.id = 0
    start.is_final = any(s in automaton.finals for s in start)
    states = [start]

    pending = [start]
    while pending:
        state = pending.pop()

        for symbol in automaton.vocabulary:
            goto = move(automaton, state, symbol)
            e_c = epsilon_closure(automaton, goto)
            if len(e_c) == 0:
                continue
            try:
                transitions[state.id, symbol]
                assert False, "Invalid DFA!!!"
            except KeyError:
                try:
                    e_c.id = states.index(e_c)
                    transitions[state.id, symbol] = e_c.id
                except ValueError:
                    e_c.id = states[-1].id + 1
                    transitions[state.id, symbol] = e_c.id
                    e_c.is_final = any(s in automaton.finals for s in e_c)
                    states.append(e_c)
                    pending.append(e_c)

    finals = [state.id for state in states if state.is_final]
    dfa = DFA(len(states), finals, transitions)
    return dfa


def PrintAutomaton(automaton, name_file, text):
    automaton.graph().write_png(name_file)
    image = Image.open(name_file)
    # st.image(image, text)


def GetDerivationTree(G, productions, of_parser_SR=False):
    if of_parser_SR:
        productions = invert_list(productions)

    stack = []
    # se asume que existe almenos una produccion aplicada por lo que se empieza con el distinguido en la pila
    start_node = State(G.startSymbol)
    stack.append(start_node)
    # siempre el no terminal al tope de la pila es el que sera esperado en la proxima produccion
    for production in productions:
        node_papa = stack.pop()
        while not node_papa.state.IsNonTerminal:
            node_papa = stack.pop()
        if not production.Left == node_papa.state:
            # Se esperaba una produccion con otro no terminal
            pass
        alpha = production.Right
        if alpha.IsEpsilon:
            node_filius = State(alpha)
            node_papa.add_epsilon_transition(node_filius)
        if not of_parser_SR:
            for i in range(len(alpha) - 1, -1, -1):
                symbol = alpha[i]
                node_filius = State(symbol)
                node_papa.add_epsilon_transition(node_filius)
                stack.append(node_filius)
        if of_parser_SR:
            for symbol in alpha:
                node_filius = State(symbol)
                node_papa.add_epsilon_transition(node_filius)
                stack.append(node_filius)
    try:
        stack[0]
    except:
        # Quedaron no terminales sin analizar
        pass

    return start_node


def invert_list(list_):
    new_list = []
    for i in range(len(list_) - 1, -1, -1):
        new_list.append(list_[i])
    return new_list
