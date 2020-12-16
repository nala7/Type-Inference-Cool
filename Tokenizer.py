from cmp.utils import Token, tokenizer
from Grammar import *

fixed_tokens = {
    t.Name: Token(t.Name, t) for t in G.terminals if t not in {idx, num, strx}
}


@tokenizer(G, fixed_tokens)
def tokenize_text(token):
    lex = token.lex
    try:
        float(lex)
        return token.transform_to(num)
    except ValueError:
        return token.transform_to(idx)


def pprint_tokens(tokens):
    indent = 0
    pending = []
    for token in tokens:
        pending.append(token)
        if token.token_type in {semi, ocur}:
            print("    " * indent + " ".join(str(t.token_type) for t in pending))
            pending.clear()
            if token.token_type == ocur:
                indent += 1
        if token.token_type in {ccur}:
            pending.pop()
            if len(pending) > 0:
                print("    " * indent + " ".join(str(t.token_type) for t in pending))
                pending.clear()
            if token.token_type == ccur:
                indent -= 1
            print("    " * indent + " ".join(str(ccur)))

    print(" ".join([str(t.token_type) for t in pending]))
