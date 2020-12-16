from cmp.utils import ContainerSet
import streamlit as st

# Computes First(alpha), given First(Vt) and First(Vn)


def compute_local_first(firsts, alpha):
    first_alpha = ContainerSet()

    try:
        alpha_is_epsilon = alpha.IsEpsilon
    except:
        alpha_is_epsilon = False

    # alpha == epsilon ? First(alpha) = { epsilon }

    if alpha_is_epsilon:
        first_alpha.set_epsilon()
        return first_alpha

    # alpha = X1 ... XN
    # First(Xi) subconjunto First(alpha)
    # epsilon pertenece a First(X1)...First(Xi) ? First(Xi+1) subconjunto de First(X) y First(alpha)
    # epsilon pertenece a First(X1)...First(XN) ? epsilon pertence a First(X) y al First(alpha)

    for x in alpha:
        first_alpha.update(firsts[x])
        if not firsts[x].contains_epsilon:
            return first_alpha

    first_alpha.set_epsilon()

    # First(alpha)
    return first_alpha


# Computes First(Vt) U First(Vn) U First(alpha)
def compute_firsts(G):
    firsts = {}
    change = True

    # init First(Vt)
    for terminal in G.terminals:
        firsts[terminal] = ContainerSet(terminal)

    # init First(Vn)
    for nonterminal in G.nonTerminals:
        firsts[nonterminal] = ContainerSet()

    while change:
        change = False

        # P: X -> alpha
        for production in G.Productions:
            X = production.Left
            alpha = production.Right

            # get current First(X)
            first_X = firsts[X]

            # init First(alpha)
            try:
                first_alpha = firsts[alpha]
            except:
                first_alpha = firsts[alpha] = ContainerSet()

            # CurrentFirst(alpha)???
            local_first = compute_local_first(firsts, alpha)

            # update First(X) and First(alpha) from CurrentFirst(alpha)
            change |= first_alpha.hard_update(local_first)
            change |= first_X.hard_update(local_first)

    # First(Vt) + First(Vt) + First(RightSides)
    return firsts


from itertools import islice


def compute_follows(G, firsts):
    follows = {}
    change = True

    local_firsts = {}

    # init Follow(Vn)
    for nonterminal in G.nonTerminals:
        follows[nonterminal] = ContainerSet()
    follows[G.startSymbol] = ContainerSet(G.EOF)

    while change:
        change = False

        # P: X -> alpha
        for production in G.Productions:
            X = production.Left
            alpha = production.Right

            follow_X = follows[X]

            # X -> zeta Y beta
            # First(beta) - { epsilon } subset of Follow(Y)
            # beta ->* epsilon or X -> zeta Y ? Follow(X) subset of Follow(Y)

            if alpha.IsEpsilon:
                continue

            if alpha[-1].IsNonTerminal:
                change |= follows[alpha[-1]].update(follows[X])

            all_epsilon = True
            for i in range(len(alpha) - 2, -1, -1):
                if alpha[i].IsTerminal:
                    all_epsilon = False
                    continue
                if all_epsilon and firsts[alpha[i + 1]].contains_epsilon:
                    change |= follows[alpha[i]].update(follows[X])
                else:
                    all_epsilon = False
                i_plus = i + 1
                first_beta = compute_local_first(firsts, alpha[i_plus:])
                change |= follows[alpha[i]].update(first_beta)

    # Follow(Vn)
    return follows


def SLPrintFirsts(G, firsts):
    firstsTerminals = {}
    for terminal in G.terminals:
        for t in firsts[terminal]:
            try:
                firstsTerminals[terminal.Name].append(t.Name)
            except:
                firstsTerminals[terminal.Name] = [t.Name]

    firstsNonTerminals = {}
    for nonTerminal in G.nonTerminals:
        for nt in firsts[nonTerminal]:
            try:
                firstsNonTerminals[nonTerminal.Name].append(nt.Name)
            except:
                firstsNonTerminals[nonTerminal.Name] = [nt.Name]

    firstsProductions = {}
    for prod in G.Productions:
        for p in firsts[prod.Right]:
            try:
                firstsProductions[str(prod.Right)].append(p.Name)
            except:
                firstsProductions[str(prod.Right)] = p.Name

    st.write("Firsts")
    st.write("Terminals", firstsTerminals)
    st.write("NonTerminals", firstsNonTerminals)
    st.write("Productions", firstsProductions)


def SLPrintFollows(G, follows):
    followsNonTerminals = {}
    for nonTerminal in G.nonTerminals:
        for nt in follows[nonTerminal]:
            try:
                followsNonTerminals[nonTerminal.Name].append(nt.Name)
            except:
                followsNonTerminals[nonTerminal.Name] = [nt.Name]

    st.write("Follows")
    st.write("NonTerminals", followsNonTerminals)
