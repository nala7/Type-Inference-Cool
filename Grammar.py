from cmp.pycompiler import Grammar
from AST.AST_Hierarchy import *

# grammar
G = Grammar()


# non-terminals
program = G.NonTerminal('<program>', startSymbol=True)
class_list, def_class = G.NonTerminals('<class-list> <def-class>')
feature_list, def_attr, def_func = G.NonTerminals('<feature-list> <def-attr> <def-func>')
param_list, other_param, param, expr_list, let_var_list = G.NonTerminals('<param-list> <other-param> <param> <expr-list> <let-var-list>')
branch_list, branch = G.NonTerminals('<branch-list> <branch>')
expr, comparer, arith, term, factor, atom = G.NonTerminals('<expr> <comparer> <arith> <term> <factor> <atom>')
func_call, obj, arg_list, other_arg  = G.NonTerminals('<func-call> <obj> <arg-list> <other-arg>')


# terminals
classx, defx, printx, inherits = G.Terminals('class def print inherits')
ifx, thenx, elsex, fi = G.Terminals('if then else fi')
whilex, loopx, poolx = G.Terminals('while loop pool')
letx, inx = G.Terminals('let in')
casex, ofx, esacx = G.Terminals('case of esac')
semi, colon, comma, dot, opar, cpar, ocur, ccur, at= G.Terminals('; : , . ( ) { } @')
equal, plus, minus, star, div, left_arrow, right_arrow, tilde = G.Terminals('= + - * / <- => ~')
less, less_equal = G.Terminals('< <=')
idx, num, new, strx, notx, isvoid, truex, falsex = G.Terminals('id Int new String not isvoid true false')


# productions
program %= class_list, lambda h,s: ProgramNode(s[1])

class_list %= def_class, lambda h,s: [s[1]]
class_list %= def_class + class_list, lambda h,s: [s[1]] + s[2]

def_class %= classx + idx + ocur + feature_list + ccur + semi, lambda h,s: ClassDeclarationNode(s[2], s[4])
def_class %= classx + idx + inherits + idx + ocur + feature_list + ccur + semi, lambda h,s: ClassDeclarationNode(s[2], s[6], s[4])

feature_list %= def_attr + feature_list, lambda h,s: [s[1]] + s[2]
feature_list %= def_func + feature_list, lambda h,s: [s[1]] + s[2]
feature_list %= G.Epsilon, lambda h,s: []

def_attr %= idx + colon + idx + semi, lambda h,s: AttrDeclarationNode(s[1], s[3])
def_attr %= idx + colon + idx + left_arrow + expr + semi, lambda h,s: AttrDeclarationNode(s[1], s[3], s[5])

def_func %= idx + opar + param_list + cpar + colon + idx + ocur + expr + ccur + semi, lambda h,s: FuncDeclarationNode(s[1], s[3], s[6], s[8])

param_list %= G.Epsilon, lambda h,s: []
param_list %= param + other_param, lambda h,s: [s[1]] + s[2]

param %= idx + colon + idx, lambda h,s: (s[1], s[3])

other_param %= G.Epsilon, lambda h,s: []
other_param %= comma + param + other_param, lambda h,s: [s[2]]+ s[3]

expr %= comparer, lambda h,s: s[1]

comparer %= comparer + less + arith, lambda h,s: LessNode(s[1], s[3])
comparer %= comparer + less_equal + arith, lambda h,s: LessEqualNode(s[1], s[3])
comparer %= comparer + equal + arith, lambda h,s: EqualNode(s[1], s[3])
comparer %= arith, lambda h,s: s[1]

arith %= arith + plus + term, lambda h,s: PlusNode(s[1], s[3])
arith %= arith + minus + term, lambda h,s: MinusNode(s[1], s[3])
arith %= term, lambda h,s: s[1]

term %= term + star + factor, lambda h,s: StarNode(s[1], s[3])
term %= term + div + factor, lambda h,s: DivNode(s[1], s[3])
term %= factor, lambda h,s: s[1]

factor %= atom, lambda h,s: s[1]

atom %= num, lambda h,s: ConstantNumNode(s[1])
atom %= idx, lambda h,s: VariableNode(s[1])
atom %= strx, lambda h,s: StringNode(s[1])
atom %= truex, lambda h,s: BoolNode(s[1])
atom %= falsex, lambda h,s: BoolNode(s[1])
atom %= opar + expr + cpar, lambda h,s: s[2]
atom %= idx + left_arrow + atom, lambda h,s: AssignNode(s[1], s[3])
atom %= new + idx, lambda h,s: InstantiateNode(s[2])
atom %= ifx + expr + thenx + expr + elsex + expr + fi, lambda h,s: ConditionalNode(s[2], s[4], s[6])
atom %= whilex + expr + loopx + expr + poolx, lambda h,s: LoopNode(s[2], s[4])
atom %= ocur + expr_list + ccur, lambda h,s: BlockNode(s[2])
atom %= letx + let_var_list + inx + atom, lambda h,s: LetNode(s[2], s[4])
atom %= casex + expr + ofx + branch_list + esacx, lambda h,s: CaseNode(s[2], s[4])
atom %= notx + atom, lambda h,s: NotNode(s[2])
atom %= isvoid + atom, lambda h,s: IsVoidNode(s[2])
atom %= tilde  + atom, lambda h,s: TildeNode(s[2])
atom %= func_call, lambda h,s: s[1]

expr_list %= expr + semi, lambda h,s: [s[1]]
expr_list %= expr + semi + expr_list, lambda h,s: [s[1]] + s[3]

let_var_list %= idx + colon + idx , lambda h,s: [(s[1],s[3],None)]
let_var_list %= idx + colon + idx + left_arrow + expr, lambda h,s: [(s[1], s[3], s[5])]
let_var_list %= idx + colon + idx + comma + let_var_list, lambda h,s: [(s[1],s[3],None)] + s[5]
let_var_list %= idx + colon + idx + left_arrow + expr + comma + let_var_list, lambda h,s: [(s[1], s[3], s[5])] + s[7]

branch_list %= idx + colon + idx + right_arrow + expr + semi, lambda h,s: [(s[1], s[3], s[5])]
branch_list %= idx + colon + idx + right_arrow + expr + semi + branch_list, lambda h,s: [(s[1], s[3], s[5])] + s[7]

func_call %= obj + dot + idx + opar + arg_list + cpar, lambda h,s: CallNode(s[1],s[3],s[5])
func_call %= idx + opar + arg_list + cpar, lambda h,s: CallNode(VariableNode('self'), s[1], s[3])
func_call %= obj + at + idx + dot + idx + opar + arg_list + cpar, lambda h,s: CallNode(s[1], s[5], s[7], s[3])

obj %= idx, lambda h,s: VariableNode(s[1])
obj %= opar + expr + cpar, lambda h,s: s[2]

arg_list %= G.Epsilon, lambda h,s: []
arg_list %= expr + other_arg, lambda h,s: [s[1]] + s[2]

other_arg %= G.Epsilon, lambda h,s: []
other_arg %= comma + expr + other_arg, lambda h,s: [s[2]] + s[3]
