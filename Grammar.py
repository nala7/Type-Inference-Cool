from AST.AST_Hierarchy import *
from cmp.pycompiler import Grammar

# grammar
G = Grammar()


# non-terminals
program = G.NonTerminal('<program>', startSymbol=True)
class_list, def_class = G.NonTerminals('<class-list> <def-class>')
feature_list, def_attr, def_func, let_var, branch = G.NonTerminals('<feature-list> <def-attr> <def-func> <let_var> <branch>')
param_list, param, expr_list, block_expr_list, let_var_list, branch_list = G.NonTerminals('<param-list> <param> <expr-list> <block_expr_list> <let_var_list> <branch_list>')
expr, arith, boolean, term, factor, atom = G.NonTerminals('<expr> <arith> <bool> <term> <factor> <atom>')
func_call, arg_list  = G.NonTerminals('<func-call> <arg-list>')


# terminals
classx, let = G.Terminals('class let')
inherits, ifx, thenx, elsex, fi, whilex, loop, pool = G.Terminals('inherits if then else fi while loop pool')
let, inx, case, of, esac, isvoid = G.Terminals('let in case of esac isvoid')
semi, colon, comma, dot, opar, cpar, ocur, ccur, quotation, tilde = G.Terminals('; : , . ( ) { } " ~')
left_arrow, right_arrow, at = G.Terminals('<- => @')
equal, plus, minus, star, div, less, less_equal = G.Terminals('= + - * / < <=')
idx, num, strx, new, notx, truex, falsex = G.Terminals('id int str new not true false')


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

param_list %= param + comma + param_list, lambda h,s: [s[1]] + s[3]
param_list %= param , lambda h,s: [s[1]] 

param %= idx + colon + idx, lambda h,s: (s[1], s[3])

expr_list %= expr, lambda h,s: [s[1]]
expr_list %= expr + comma + expr_list, lambda h,s: [s[1]] + s[3]

expr %= ifx + expr + thenx + expr + elsex + expr + fi, lambda h,s: CondNode(s[2], s[4], s[6])

expr %= whilex + expr + loop + expr + pool, lambda h,s: LoopNode(s[2], s[4])

expr %= ocur + block_expr_list + ccur, lambda h,s: BlockNode(s[2])

block_expr_list %= expr + semi, lambda h,s: [s[1]]
block_expr_list %= expr + semi + block_expr_list, lambda h,s: [s[1]] + s[3]

expr %= let + let_var_list + inx + expr, lambda h,s: LetNode(s[2], s[4])

let_var_list %= let_var, lambda h,s: [s[1]]
let_var_list %= let_var + comma + let_var_list, lambda h,s: [s[1]] + s[3]
let_var %= idx + colon + idx, lambda h,s: (s[1], s[3], None)
let_var %= idx + colon + idx + left_arrow + expr, lambda h,s: (s[1], s[3], s[5])

expr %= case + expr + of + branch_list + esac, lambda h,s: CaseNode(s[2], s[4])

branch_list %= branch, lambda h,s:[s[1]]
branch_list %= branch + branch_list, lambda h,s: [s[1]] + s[2]
branch %= idx + colon + idx + right_arrow + expr + semi, lambda h,s: (s[1], s[3], s[5])

expr %= new + idx, lambda h,s: InstantiateNode(s[2])

expr %= arith, lambda h,s: s[1]

arith %= arith + plus + term, lambda h,s: PlusNode(s[1], s[3])
arith %= arith + minus + term, lambda h,s: MinusNode(s[1], s[3])
arith %= arith + less + term, lambda h,s: LessNode(s[1], s[3])
arith %= arith + less_equal + term, lambda h,s: LessEqualNode(s[1], s[3])
arith %= arith + equal + term, lambda h,s: EqualNode(s[1], s[3])
arith %= arith + expr, lambda h,s: NotNode(s[2])

arith %= term, lambda h,s: s[1]

term %= term + star + factor, lambda h,s: StarNode(s[1], s[3])
term %= term + div + factor, lambda h,s: DivNode(s[1], s[3])
term %= factor, lambda h,s: s[1]

factor %= atom, lambda h,s: s[1]
factor %= opar + expr + cpar, lambda h,s: s[2]

atom %= num, lambda h,s: ConstantNumNode(s[1])
atom %= idx, lambda h,s: VariableNode(s[1])
atom %= truex, lambda h,s: BoolNode(s[1])
atom %= quotation + strx + quotation, lambda h,s: StringNode(strx)
atom %= idx + left_arrow + atom, lambda h,s: AssignNode(s[1], s[3])
atom %= isvoid + atom, lambda h,s: IsVoidNode(s[2])
atom %= notx + atom, lambda h,s: NotNode(s[2])
atom %= tilde + atom, lambda h,s: ComplementNode(s[2])
atom %= func_call, lambda h,s: s[1]


func_call %= expr + dot + idx + opar + expr_list + cpar, lambda h,s: CallNode(s[1], s[3], s[5])
func_call %= idx + opar + expr_list + cpar, lambda h,s: CallNode('SELF_TYPE', s[1], s[3])
func_call %= expr + at + idx + dot + idx + opar + expr_list + cpar, lambda h,s: CallNode(s[1], s[5], s[7], s[3])


if __name__ == '__main__': print(G)
