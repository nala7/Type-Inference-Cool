from inspect import currentframe
import cmp.visitor as visitor
from cmp.semantic import Scope, StrType
from cmp.semantic import SemanticError
from cmp.semantic import Attribute, Method, Type
from cmp.semantic import SelfType, AutoType
from cmp.semantic import VoidType, ErrorType, IntType, BoolType, ObjType
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
        self.scope_id = 0

    @visitor.on('node')
    def visit(self, node, scope):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, scope=None):
        scope = Scope(self.scope_id)
        self.scope_id += 1
        for declaration in node.declarations:
            child_scope = scope.create_child(self.scope_id)
            self.scope_id += 1
            self.visit(declaration, child_scope)
        return scope

    @visitor.when(ClassDeclarationNode)
    def visit(self, node, scope):
        # print('class declaration')
        scope.define_variable('self', SelfType())
        self.current_type = self.context.get_type(node.id)
        for feature in node.features:
            self.visit(feature, scope)
        
    @visitor.when(AttrDeclarationNode)#
    def visit(self, node:AttrDeclarationNode, scope:Scope):
        # print('attr declaration')
        var = scope.my_find_var(node.id)
        attr_type = self.context.get_type(node.type)
        if var is not None:
            self.errors.append(ATTR_ALREADY_DEFINED % (node.id))
        else:
            scope.define_variable(node.id, attr_type)
        
        if node.val is not None: 
            return_type = self.visit(node.val, scope) 
        else: 
            return_type = attr_type

        if attr_type == SelfType():
            to_conform = self.current_type
        else:
            to_conform = attr_type

        if not return_type.conforms_to(to_conform):
            self.errors.append(INCOMPATIBLE_TYPES % (return_type.name, to_conform.name))

        return attr_type

    @visitor.when(FuncDeclarationNode)#
    def visit(self, node, scope):
        # print('function declaration')
        method = self.current_type.get_method(node.id)
        self.current_method = method
        
        if self.current_type.parent is not None:
            try:
                ancestor_method = self.current_type.parent.get_method(node.id)
                if not method == ancestor_method:
                    self.errors.append(WRONG_SIGNATURE % (node.id, 'ancestor type'))
            except SemanticError:
                ancestor_method = None
        
        child_scope = scope.create_child(self.scope_id)
        self.scope_id += 1
        for i in range(0, len(method.param_names)):
            child_scope.define_variable(method.param_names[i], method.param_types[i])
        
        expr_type = self.visit(node.body, child_scope)
        if method.return_type == SelfType():
            to_conform = self.current_type
        else:
            to_conform = method.return_type
        if not expr_type.conforms_to(to_conform):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, to_conform.name))

    @visitor.when(ConditionalNode)#
    def visit(self, node, scope):
        # print('conditional')
        cond_type = self.visit(node.if_expr, scope)
        if not cond_type.conforms_to(BoolType()):
            self.errors.append(INCOMPATIBLE_TYPES % (cond_type.name, BoolType().name))

        then_expr_type = self.visit(node.then_expr, scope)
        else_expr_type = self.visit(node.else_expr, scope)
        
        common_ancestor_type = self.context.find_first_common_ancestor(then_expr_type, else_expr_type)

        return common_ancestor_type
            
    @visitor.when(LoopNode)#
    def visit(self, node, scope):
        # print('loop')
        cond_type = self.visit(node.condition, scope)
        if not cond_type.conforms_to(BoolType()):
            self.errors.append(INCOMPATIBLE_TYPES % (cond_type.name, BoolType().name))
        
        self.visit(node.body, scope)

        return ObjType()
    
    @visitor.when(BlockNode)#
    def visit(self, node : BlockNode, scope):
        # print('block')
        child_scope = scope.create_child(self.scope_id)
        self.scope_id += 1
        return_type = ErrorType()
        for expr in node.expr_list:
            return_type = self.visit(expr, child_scope)

        return return_type

    @visitor.when(LetNode)#
    def visit(self, node, scope):
        # print('let')
        child_scope = scope
        for var, typex, expr in node.var_list:
            child_scope = child_scope.create_child(self.scope_id)
            self.scope_id += 1
            try:
                var_type = self.context.get_type(typex)
            except SemanticError as error:
                self.errors.append(error.text)
                var_type = ErrorType()

            if expr is not None:
                expr_type = self.visit(expr, child_scope)
            else:
                expr_type = var_type

            if var_type == SelfType():
                to_conform = self.current_type
            else:
                to_conform = var_type
            if not expr_type.conforms_to(to_conform):
                self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, to_conform.name))

            child_scope.define_variable(var, var_type)

        return self.visit(node.body, child_scope)

    @visitor.when(CaseNode)#
    def visit(self, node, scope):
        # print('case')
        self.visit(node.expr, scope)

        types_used = set()
        return_type = None
        # child_scope = scope.create_child(self.scope_id)
        # self.scope_id += 1
        for var, typex, expr in node.branch_list:
            try:
                var_type = self.context.get_type(typex)
            except SemanticError as error:
                self.errors.append(error.text)
                var_type = ErrorType()
            
            if var_type != ErrorType():
                if var_type.name in types_used:
                    self.errors.append(f'In method {self.current_method.name}, type {self.current_type.name} more than one branch variables have type {var_type.name}')
                types_used.add(var_type.name)
            
            child_scope = scope.create_child(self.scope_id)
            self.scope_id += 1
            expr_type = self.visit(expr, child_scope)
            if not expr_type.conforms_to(var_type):
                self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, var_type.name))

            if return_type is None:
                return_type = var_type
            return_type = self.context.find_first_common_ancestor(var_type, return_type)

            child_scope.define_variable(var, var_type)
        return return_type

    @visitor.when(AssignNode)
    def visit(self, node, scope:Scope):
        # print('assign')        
        var = scope.my_find_var(node.id)
        if var is None:    
            self.errors.append(VARIABLE_NOT_DEFINED % (node.id, self.current_method.name))
            var_type = ErrorType()
        else:
            var_type = var.type
        
        expr_type = self.visit(node.expr, scope)
        if not expr_type.conforms_to(var_type):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, var_type.name))
        
        return expr_type

    @visitor.when(CallNode)#
    def visit(self, node, scope):
        # print('call')
        obj_type = self.visit(node.obj, scope)
        t0 = obj_type
        if t0 == SelfType:
            t0 = self.current_type
        # if obj_type.name == AutoType().name:
        #     self.errors.append('Method '+id+' not callable')
        
        if node.ancestor_type is not None:
            ancestor_type = self.context.get_type(node.ancestor_type)
            if not t0.conforms_to(ancestor_type):
                self.errors.append(f'Type {t0.name} no conforms to {ancestor_type.name}')
            t0 = ancestor_type
   
        try:
            method = t0.get_method(node.id)
        except SemanticError as error:
            self.errors.append(error.text)
            return ErrorType()

        if not len(method.param_names) == len(node.args):
            self.errors.append(METHOD_ARGS_UNMATCH % (method.name))
        else:
            for i in range(0, len(node.args)):
                arg_type = self.visit(node.args[i], scope)
                if not arg_type.conforms_to(method.param_types[i]):
                    self.errors.append(INCOMPATIBLE_TYPES % (arg_type.name, method.param_types[i].name))
        
        if method.return_type == SelfType():
            return obj_type
        return method.return_type
            
    @visitor.when(ArithBinaryNode)#
    def visit(self, node, scope):
        # print('arith binary')
        left_type = self.visit(node.left, scope)
        right_type = self.visit(node.right, scope)
        int_type = IntType()
        if not left_type.conforms_to(int_type) or not right_type.conforms_to(int_type):
            self.errors.append(INVALID_OPERATION % (left_type.name, right_type.name))
        return int_type
        
    @visitor.when(BooleanBinaryNode)#
    def visit(self, node, scope):
        # print('boolean binary')
        left_type = self.visit(node.left, scope)
        right_type = self.visit(node.right, scope)

        if isinstance(node, EqualNode):
            if (left_type.name in {'int', 'str', 'bool'} or right_type.name in {'int', 'str', 'bool'}) and left_type != right_type:
                self.errors.append(INVALID_OPERATION % (left_type.name, right_type.name))
            return BoolType()

        int_type = IntType()
        if not left_type.conforms_to(int_type) or not right_type.conforms_to(int_type):
            self.errors.append(INVALID_OPERATION % (left_type.name, right_type.name))
        return BoolType()

    @visitor.when(ConstantNumNode)#
    def visit(self, node, scope):
        # print('constant')
        return IntType()

    @visitor.when(BoolNode)#
    def visit(self, node, scope):
        # print('bool')
        return BoolType()

    @visitor.when(VariableNode)
    def visit(self, node, scope:Scope):
        # print('variable')
        var = scope.my_find_var(node.lex)
        if var is None:
            self.errors.append(VARIABLE_NOT_DEFINED%(node.lex,self.current_method.name))
            return ErrorType()
        else:
            var_type = var.type
            return var_type

    @visitor.when(InstantiateNode)#
    def visit(self, node, scope):
        # print('instantiate')
        try:
            instance_type = self.context.get_type(node.lex)
        except SemanticError as error:
            self.errors.append(error.text)
            instance_type = ErrorType()
        return instance_type
    
    @visitor.when(NotNode)#
    def visit(self, node, scope):
        # print('not node')
        expr_type = self.visit(node.expr, scope)
        if not expr_type.conforms_to(BoolType()):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, BoolType().name))
        return BoolType()

    @visitor.when(IsVoidNode)#
    def visit(self, node, scope):
        # print('is void')
        self.visit(node.expr, scope)
        return BoolType()

    @visitor.when(TildeNode)#
    def visit(self, node, scope):
        # print('tilde')
        expr_type = self.visit(node.expr, scope)
        if not expr_type.conforms_to(IntType()):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, IntType().name))
        
        return IntType()
