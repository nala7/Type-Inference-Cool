import cmp.visitor as visitor
from cmp.semantic import Scope
from cmp.semantic import SemanticError
from cmp.semantic import Attribute, Method, Type
from cmp.semantic import VoidType, ErrorType, IntType
from cmp.semantic import Context
from AST.AST_Hierarchy import *


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
    def visit(self, node, scope):
        #print('attr declaration')
        var = self.find_var(node.id,scope)
        if var is not None:
            self.errors.append(ATTR_ALREADY_DEFINED % (node.id))
        else:
            attr_type = self.context.get_type(node.type)
            scope.define_variable(node.id, attr_type)

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
        
        expr_type = None
        for expr in node.body:
            expr_type = self.visit(expr, child_scope)
        if self.current_method.return_type.name != VoidType().name and not self.current_method.return_type.conforms_to(expr_type):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name ,self.current_method.return_type.name))

        
    @visitor.when(VarDeclarationNode)
    def visit(self, node, scope):
        #print('var declaraion')
        try:
            var_type = self.context.get_type(node.type)
        except SemanticError as error:
            self.errors.append(error.text)
            var_type = ErrorType()
        
        if scope.is_local(node.id):
            self.errors.append(LOCAL_ALREADY_DEFINED % (node.id,self.current_method.name))
        else:
            scope.define_variable(node.id, var_type)
        expr_type = self.visit(node.expr, scope)
        if not var_type.conforms_to(expr_type):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, var_type.name))
        
        return var_type
            
    @visitor.when(AssignNode)
    def visit(self, node, scope):
        #print('assign')
        
        var = self.find_var(node.id, scope)
        if var is None:    
            self.errors.append(VARIABLE_NOT_DEFINED % (node.id,self.current_method.name))
            var_type = ErrorType()
        else:
            var_type = var.type
        
        expr_type = self.visit(node.expr, scope)
        if not var_type.conforms_to(expr_type):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, var_type.name))
        
        return var_type
    
    
    @visitor.when(CallNode)
    def visit(self, node, scope):
        #print('call')
        obj_type = self.visit(node.obj, scope)
        method = obj_type.get_method(node.id)
        if not len(method.param_names) == len(node.args):
            self.errors.append(METHOD_ARGS_UNMATCH % (method.name))
        else:
            for i in range(0, len(node.args)):
                arg_type = self.visit(node.args[i], scope)
                if not arg_type == method.param_types[i]:
                    self.errors.append(INCOMPATIBLE_TYPES % (arg_type.name, method.param_types[i].name))
        
        return method.return_type
            
            
    @visitor.when(BinaryNode)
    def visit(self, node, scope):
        #print('binary')
        left_type = self.visit(node.left, scope)
        right_type = self.visit(node.right, scope)
        int_type = IntType()
        if left_type != int_type or right_type != int_type:
            self.errors.append(INVALID_OPERATION % (left_type.name, right_type.name))
        return int_type
        
        
    @visitor.when(ConstantNumNode)
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