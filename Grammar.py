from cmp.pycompiler import Grammar
from AST.AST_Hierarchy import *

# grammar
G = Grammar()


# non-terminals
program = G.NonTerminal('<program>', startSymbol=True)
class_list, def_class = G.NonTerminals('<class-list> <def-class>')
feature_list, def_attr, def_func = G.NonTerminals('<feature-list> <def-attr> <def-func>')
param_list, param, expr_list, let_var_list = G.NonTerminals('<param-list> <param> <expr-list> <let-var-list>')
branch_list, branch = G.NonTerminals('<branch-list> <branch>')
expr, arith, term, factor, compare, atom = G.NonTerminals('<expr> <arith> <term> <factor> <atom>')
func_call, arg_list  = G.NonTerminals('<func-call> <arg-list>')


# terminals
classx, defx, printx, inherits = G.Terminals('class def print inherits')
ifx, thenx, elsex, fi = G.Terminals('if then else fi')
whilex, loopx, poolx = G.Terminals('while loop pool')
letx, inx = G.Terminals('let in')
casex, ofx, esacx = G.Terminals('case of esac')
semi, colon, comma, dot, opar, cpar, ocur, ccur, at= G.Terminals('; : , . ( ) { } @')
equal, plus, minus, star, div, left_arrow, right_arrow, tilde = G.Terminals('= + - * / <- => ~')
less, less_equal = G.Terminals('< <=')
idx, num, new, notx, isvoid, truex, falsex = G.Terminals('id int new not isvoid true false')


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

def_func %= defx + idx + opar + param_list + cpar + colon + idx + ocur + expr + ccur + semi, lambda h,s: FuncDeclarationNode(s[2], s[4], s[7], s[9])

param_list %= param, lambda h,s: [ s[1] ]
param_list %= param + comma + param_list, lambda h,s: [ s[1] ] + s[3]

param %= idx + colon + idx, lambda h,s: (s[1], s[3])

expr %= ifx + expr + thenx + expr + elsex + expr + fi, lambda h,s: ConditionalNode(s[2], s[4], s[6])
expr %= whilex + expr + loopx + expr + poolx, lambda h,s: LoopNode(s[2], s[4])
expr %= ocur + expr_list + ccur, lambda h,s: BlockNode(s[2])
expr %= letx + let_var_list + inx + expr, lambda h,s: LetNode(s[2], s[4])
expr %= casex + expr + ofx + branch_list + esacx, lambda h,s: CaseNode(s[2], s[4])
# expr %= notx + expr, lambda h,s: NotNode(s[2])
# expr %= isvoid + expr, lambda h,s: IsVoidNode(s[2])
# expr %= tilde  + expr, lambda h,s: TildeNode(s[2])
expr %= func_call, lambda h,s: s[1]
expr %= arith, lambda h,s: s[1]


expr_list %= expr + semi, lambda h,s: [s[1]]
expr_list %= expr + semi + expr_list, lambda h,s: [s[1]] + s[3]

let_var_list %= param , lambda h,s: [(s[1],None)]
let_var_list %= param + left_arrow + expr, lambda h,s: [(s[1], s[3])]
let_var_list %= param + comma + let_var_list, lambda h,s: [(s[1],None)] + s[3]
let_var_list %= param + left_arrow + expr + comma + let_var_list, lambda h,s: [(s[1],s[3])] + s[5]

branch_list %= param + right_arrow + expr + semi, lambda h,s: [(s[1], s[3])]
branch_list %= param + right_arrow + expr + semi + branch_list, lambda h,s: [(s[1], s[3])] + s[5]

func_call %= expr + dot + idx + opar + arg_list + cpar, lambda h,s: CallNode(s[1],s[3],s[5])
func_call %= idx + opar + arg_list + cpar, lambda h,s: CallNode('SELF_TYPE', s[1], s[3])
func_call %= expr + at + idx + dot + idx + opar + arg_list + cpar, lambda h,s: CallNode(s[1], s[5], s[7], s[3])

arith %= arith + plus + term, lambda h,s: PlusNode(s[1], s[3])
arith %= arith + minus + term, lambda h,s: MinusNode(s[1], s[3])
arith %= term, lambda h,s: s[1]

term %= term + star + factor, lambda h,s: StarNode(s[1], s[3])
term %= term + div + factor, lambda h,s: DivNode(s[1], s[3])
term %= factor, lambda h,s: s[1]

factor %= atom, lambda h,s: s[1]
factor %= opar + expr + cpar, lambda h,s: s[2]

compare %= compare + less + atom, lambda h,s: LessNode(s[1], s[3])
compare %= compare + less_equal + atom, lambda h,s: LessEqualNode(s[1], s[3])
compare %= compare + equal + atom, lambda h,s: EqualNode(s[1], s[3])

atom %= num, lambda h,s: ConstantNumNode(s[1])
atom %= idx, lambda h,s: VariableNode(s[1])
atom %= truex, lambda h,s: BoolNode(s[1])
atom %= falsex, lambda h,s: BoolNode(s[1])
atom %= new + idx, lambda h,s: InstantiateNode(s[2])



arg_list %= expr, lambda h,s: [ s[1] ]
arg_list %= expr + comma + arg_list, lambda h,s: [ s[1] ] + s[3]
