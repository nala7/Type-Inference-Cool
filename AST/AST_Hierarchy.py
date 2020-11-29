class Node:
    pass
    
class ProgramNode(Node):
    def __init__(self, declarations):
        self.declarations = declarations

class DeclarationNode(Node):
    pass
class ExpressionNode(Node):
    pass

class ClassDeclarationNode(DeclarationNode):
    def __init__(self, idx, features, parent=None):
        self.id = idx
        self.parent = parent
        self.features = features

class FuncDeclarationNode(DeclarationNode):
    def __init__(self, idx, params, return_type, body):
        self.id = idx
        self.params = params
        self.type = return_type
        self.body = body

class AttrDeclarationNode(DeclarationNode):
    def __init__(self, idx, typex, expr = None):
        self.id = idx
        self.type = typex
        self.expr = expr

class AssignNode(ExpressionNode):
    def __init__(self, idx, expr):
        self.id = idx
        self.expr = expr

class CallNode(ExpressionNode):
    def __init__(self, obj, idx, args, ancestor = None):
        self.obj = obj
        self.id = idx
        self.args = args
        self.ancestor = ancestor

class CondNode(ExpressionNode):
    def __init__(self, if_expr, then_expr, else_expr):
        self.if_expr = if_expr
        self.then_expr = then_expr
        self.else_expr = else_expr

class LoopNode(ExpressionNode):
    def __init__(self, cond_expr, body):
        self.cond = cond_expr
        self.body = body

class BlockNode(ExpressionNode):
    def __init__(self, expr_list):
        self.expr_list = expr_list

class LetNode(ExpressionNode):
    def __init__(self, var_list, body):
        self.var_list = var_list
        self.body = body

class CaseNode(ExpressionNode):
    def __init__(self, expr, branch_list):
        self.expr = expr
        self.branch_list = branch_list

class IsVoidNode(ExpressionNode):
    def __init__(self, expr):
        self.expr = expr

class NotNode(ExpressionNode):
    def __init__(self, expr):
        self.expr = expr

class ComplementNode(ExpressionNode):
    def __init__(self, expr):
        self.expr = expr

class AtomicNode(ExpressionNode):
    def __init__(self, lex):
        self.lex = lex

class BinaryNode(ExpressionNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class ConstantNumNode(AtomicNode):
    pass
class VariableNode(AtomicNode):
    pass
class StringNode(AtomicNode):
    pass
class BoolNode(AtomicNode):
    pass
class InstantiateNode(AtomicNode):
    pass
class PlusNode(BinaryNode):
    pass
class MinusNode(BinaryNode):
    pass
class StarNode(BinaryNode):
    pass
class DivNode(BinaryNode):
    pass
class LessNode(BinaryNode):
    pass
class LessEqualNode(BinaryNode):
    pass
class EqualNode(BinaryNode):
    pass