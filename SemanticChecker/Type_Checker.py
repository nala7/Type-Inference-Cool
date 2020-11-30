import cmp.visitor as visitor
from cmp.semantic import Scope
from cmp.semantic import SemanticError
from cmp.semantic import Attribute, Method, Type
from cmp.semantic import VoidType, ErrorType, IntType, BoolType, ObjType
from cmp.semantic import Context
from AST.AST_Hierarchy import *
from cmp.utils import find_first_common_ancestor


WRONG_SIGNATURE = 'Method "%s" already defined in "%s" with a different signature.'
SELF_IS_READONLY = 'Variable "self" is read-only.'
LOCAL_ALREADY_DEFINED = 'Variable "%s" is already defined in method "%s".'
ATTR_ALREADY_DEFINED = 'Attribute "%s" is already defined in ancestor class.'
INCOMPATIBLE_TYPES = 'Cannot convert "%s" into "%s".'
VARIABLE_NOT_DEFINED = 'Variable "%s" is not defined in "%s".'
INVALID_OPERATION = 'Operation is not defined between "%s" and "%s".'
METHOD_ARGS_UNMATCH = 'Method "%s" arguments do not match with definition.'


class TypeChecker:
    def __init__(self, context, errors=[]):
        self.context = context
        self.current_type = None
        self.current_method = None
        self.errors = errors

    @visitor.on('node')
    def visit(self, node, scope):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        scope = Scope()
        for declaration in node.declarations:
            self.visit(declaration, scope.create_child())
        return scope

    @visitor.when(ClassDeclarationNode)
    def visit(self, node, scope):
        #print('class declaration')
        self.current_type = self.context.get_type(node.id)
        for feature in node.features:
            self.visit(feature, scope)
        
    @visitor.when(AttrDeclarationNode)
    def visit(self, node:AttrDeclarationNode, scope):
        #print('attr declaration')
        var = self.find_var(node.id,scope)
        attr_type = self.context.get_type(node.type)
        if var is not None:
            self.errors.append(ATTR_ALREADY_DEFINED % (node.id))
        else:
            scope.define_variable(node.id, attr_type)
        
        if node.val is not None: 
            return_type = self.visit(node.val, scope) 
        else: 
            return_type = attr_type

        #lo cambie, me parece q es al reves el conforms
        if not return_type.conforms_to(attr_type):
            self.errors.append(INCOMPATIBLE_TYPES % (return_type.name, attr_type.name))

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, scope):
        #print('function declaration')
        method = self.current_type.get_method(node.id)
        self.current_method = method
        
        if self.current_type.parent is not None:
            try:
                ancestor_method = self.current_type.parent.get_method(node.id)
                if not method == ancestor_method:
                    self.errors.append(WRONG_SIGNATURE % (node.id, 'ancestor type'))
            except SemanticError:
                ancestor_method = None
        
        child_scope = scope.create_child()
        for i in range(0, len(method.param_names)):
            child_scope.define_variable(method.param_names[i], method.param_types[i])
        
        expr_type = self.visit(node.body, child_scope)
        #pa mi las expresiones q son void retornan VoidType
        if self.current_method.return_type.name != VoidType().name and not self.current_method.return_type.conforms_to(expr_type):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name ,self.current_method.return_type.name))

    @visitor.when(ConditionalNode)
    def visit(self, node, scope):
        cond_type = self.visit(node.if_expr, scope)
        if not cond_type == BoolType():
            self.errors.append(INCOMPATIBLE_TYPES % (cond_type, BoolType()))

        then_expr_type = self.visit(node.then_expr, scope)
        else_expr_type = self.visit(node.else_expr, scope)
        
        #siempre tienen en comun obj (no se como funciona este metodo esta al berro)
        #if == AUTO_TYPE ????
        common_ancestor_type = find_first_common_ancestor(then_expr_type, else_expr_type)

        return common_ancestor_type
            
    @visitor.when(LoopNode)
    def visit(self, node, scope):
        cond_type = self.visit(node.condition, scope)
        if not cond_type == BoolType():
            self.errors.append(INCOMPATIBLE_TYPES % (cond_type, BoolType()))
        
        #me parece q no hay q hacer mas nada
        self.visit(node.body, scope)

        return ObjType()
    
    @visitor.when(BlockNode)
    def visit(self, node, scope):
        for expr in node.expr_list:
            return_type = self.visit(expr, scope)

        return return_type

    @visitor.when(LetNode)
    def visit(self, node, scope):
        for var, typex, expr in node.var_list:
            expr_type = None
            if expr is not None:
                expr_type = self.visit(expr)
            scope.define_variable(var, typex)

        pass

    @visitor.when(CaseNode)
    def visit(self, node, scope):
        pass

    @visitor.when(AssignNode)
    def visit(self, node, scope):
        #print('assign')
        
        var = self.find_var(node.id, scope)
        if var is None:    
            self.errors.append(VARIABLE_NOT_DEFINED % (node.id, self.current_method.name))
            var_type = ErrorType()
        else:
            var_type = var.type
        
        expr_type = self.visit(node.expr, scope)
        #al reves conforms???
        if not expr_type.conforms_to(var_type):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, var_type.name))
        
        #retorna el type d la expr (manual)
        return expr_type

    @visitor.when(CallNode)
    def visit(self, node, scope):
        #print('call')
        ancestor = Context.get_type(node.ancestor) 
        if ancestor is not None:
            call_type = ancestor
        else:
            call_type = self.visit(node.obj, scope)
        
        method = call_type.get_method(node.id)
        if not len(method.param_names) == len(node.args):
            self.errors.append(METHOD_ARGS_UNMATCH % (method.name))
        else:
            for i in range(0, len(node.args)):
                arg_type = self.visit(node.args[i], scope)
                if not arg_type == method.param_types[i]:
                    self.errors.append(INCOMPATIBLE_TYPES % (arg_type.name, method.param_types[i].name))
        
        return method.return_type
            
            
    @visitor.when(ArithBinaryNode)
    def visit(self, node, scope):
        #print('binary')
        left_type = self.visit(node.left, scope)
        right_type = self.visit(node.right, scope)
        int_type = IntType()
        if left_type != int_type or right_type != int_type:
            self.errors.append(INVALID_OPERATION % (left_type.name, right_type.name))
        return int_type
        
    @visitor.when(BooleanBinaryNode)
    def visit(self, node, scope):
        #print('binary')
        left_type = self.visit(node.left, scope)
        right_type = self.visit(node.right, scope)
        bool_type = BoolType()
        if left_type != bool_type or right_type != bool_type:
            self.errors.append(INVALID_OPERATION % (left_type.name, right_type.name))
        return bool_type

    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        #print('constant')
        return IntType()

    @visitor.when(NotNode)
    def visit(self, node, scope):
        #print('constant')
        return BoolType()

    @visitor.when(IsVoidNode)
    def visit(self, node, scope):
        #print('constant')
        return BoolType()

    @visitor.when(TildeNode)
    def visit(self, node, scope):
        #print('constant')
        return IntType()

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        #print('variable')
        
        var = self.find_var(node.lex, scope)
        if var is None:
            self.errors.append(VARIABLE_NOT_DEFINED%(node.lex,self.current_method.name))
            return ErrorType()
        else:
            var_type = var.type
            return var_type

    @visitor.when(InstantiateNode)
    def visit(self, node, scope):
        #print('instantiate')
        try:
            instance_type = self.context.get_type(node.lex)
        except SemanticError as error:
            self.errors.append(error.text)
            instance_type = ErrorType()
        return instance_type
    


    def find_var(self, vname, scope):
        s = scope
        while s is not None:
            for local in s.locals:
                if local.name == vname:
                    return local
            s = s.parent
        return None