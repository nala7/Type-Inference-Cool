# from pandas import DataFrame


class ShiftReduceParser:
    SHIFT = "SHIFT"
    REDUCE = "REDUCE"
    OK = "OK"

    def __init__(self, G, verbose=False, build_parsing_table=True):
        self.G = G
        self.verbose = verbose
        self.action = {}
        self.goto = {}
        self.conflict = False
        if build_parsing_table:
            self._build_parsing_table()

    def _build_parsing_table(self):
        raise NotImplementedError()

    def __call__(self, w, get_shift_reduce=False):
        if self.conflict:
            print("Conflicts encountered in grammar")
            return None
        stack = [0]
        cursor = 0
        output = []
        operations = []

        while True:
            state = stack[-1]
            lookahead = w[cursor]
            if self.verbose:
                print(stack, "<---||--->", w[cursor:])

            if not (state, lookahead.Name) in self.action:
                return None

            action, tag = self.action[state, lookahead.Name]
            if action == self.SHIFT:
                operations.append("SHIFT")
                stack.append(tag)
                cursor += 1
            elif action == self.REDUCE:
                operations.append("REDUCE")
                length = len(tag.Right)
                while length > 0:
                    stack.pop()
                    length -= 1
                output.append(tag)
                last = stack[-1]
                stack.append(self.goto[last, tag.Left.Name])
            elif action == self.OK:
                if get_shift_reduce:
                    return output, operations
                return output
            else:
                assert False, "Error"
                break


def encode_value(value):
    try:
        action, tag = value
        if action == ShiftReduceParser.SHIFT:
            return "S" + str(tag)
        elif action == ShiftReduceParser.REDUCE:
            return repr(tag)
        elif action == ShiftReduceParser.OK:
            return action
        else:
            return value
    except TypeError:
        return value


# def table_to_dataframe(table):
#     d = {}
#     for (state, symbol), value in table.items():
#         value = encode_value(value)
#         try:
#             d[state][symbol] = value
#         except KeyError:
#             d[state] = {symbol: value}
#
#     return DataFrame.from_dict(d, orient="index", dtype=str)
