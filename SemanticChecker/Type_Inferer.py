import cmp.visitor as visitor
from cmp.semantic import Scope, SelfType
from cmp.semantic import SemanticError
from cmp.semantic import Attribute, Method, Type
from cmp.semantic import VoidType, ErrorType, IntType, BoolType, ObjType
from cmp.semantic import Context
from AST.AST_Hierarchy import *

VAR_AUTOTYPE = 'Variable "%s" type not infered in "%s".'
METH_AUTOTYPE = 'Method "%s" return type not infered in "%s"'

class TypeInferer:
    def __init__(self, context, errors=[]):
        self.context = context
        self.current_type = None
        self.current_method = None
        self.errors = errors
        self.autotypes = []
    
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
        print('class declaration')
        self.current_type = self.context.get_type(node.id)
        for feature in node.features:
            self.visit(feature, scope)

        
    @visitor.when(AttrDeclarationNode)
    def visit(self, node:AttrDeclarationNode, scope):
        print('attr declaration')
        attr_type = self.context.get_type(node.type)
        if node.val is not None: 
            return_type = self.visit(node.val, scope) 
            if attr_type.name == AutoType().name:
                attr_type = return_type
        else: 
            return_type = attr_type
        
        var = scope.define_variable(node.id, attr_type)
        
        if return_type.name == AutoType().name:
            self.autotypes.append(VAR_AUTOTYPE % (var.name, self.current_type.name))

        return attr_type

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, scope):
        print('function declaration')
        method = self.current_type.get_method(node.id)
        self.current_method = method
        
        child_scope = scope.create_child()
        for i in range(0, len(method.param_names)):
            child_scope.define_variable(method.param_names[i], method.param_types[i])
        
        expr_type = self.visit(node.body, child_scope)
        if method.return_type.name == AutoType().name:
            method.return_type = expr_type
            if expr_type.name == AutoType().name:
                self.autotypes.append(METH_AUTOTYPE % (method.name, self.current_type.name))
        

        if self.current_method.return_type.name != VoidType().name and not self.current_method.return_type.conforms_to(expr_type):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name ,self.current_method.return_type.name))
        # if self.current_method.return_type.name == VoidType().name and expr_type.name != VoidType().name:
            # self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, VoidType().name))

    @visitor.when(ConditionalNode)
    def visit(self, node, scope):
        print('conditional')
        cond_type = self.visit(node.if_expr, scope)

        then_expr_type = self.visit(node.then_expr, scope)
        else_expr_type = self.visit(node.else_expr, scope)
        
        common_ancestor_type = self.context.find_first_common_ancestor(then_expr_type, else_expr_type)

        return common_ancestor_type
            
    @visitor.when(LoopNode)
    def visit(self, node, scope):
        print('loop')
        
        self.visit(node.condition, scope)
        
        self.visit(node.body, scope)

        return VoidType()
    
    @visitor.when(BlockNode)
    def visit(self, node, scope):
        print('block')
        child_scope = scope.create_child()
        for expr in node.expr_list:
            return_type = self.visit(expr, child_scope)

        return return_type

    @visitor.when(LetNode)
    def visit(self, node, scope):
        print('let')
        child_scope = scope.create_child()
        for var, typex, expr in node.var_list:
            child_scope = child_scope.create_child()
            try:
                var_type = self.context.get_type(typex)
            except SemanticError as error:
                self.errors.append(error.text)
                var_type = ErrorType()

            if expr is not None:
                expr_type = self.visit(expr, child_scope)
            else:
                expr_type = var_type

            #Check autotype
            if not var_type.conforms_to(expr_type):
                self.errors.append(INCOMPATIBLE_TYPES % (var_type.name, expr_type.name))

            child_scope.define_variable(var, var_type)

        print(node.body)
        return self.visit(node.body, child_scope)

    @visitor.when(CaseNode)
    def visit(self, node, scope):
        print('case')
        self.visit(node.expr, scope)

        return_type = None
        child_scope = scope.create_child()
        for var, typex, expr in node.branch_list:
            try:
                var_type = self.context.get_type(typex)
            except SemanticError as error:
                self.errors.append(error.text)
                var_type = ErrorType()
            
            if return_type is None:
                return_type = var_type

            
            child_scope = child_scope.create_child()
            expr_type = self.visit(expr, child_scope)
            if not var_type.conforms_to(expr_type):
                self.errors.append(INCOMPATIBLE_TYPES % (var_type.name, expr_type.name))

            return_type = self.context.find_first_common_ancestor(var_type, return_type)

            scope.define_variable(var, var_type)
        return return_type

    @visitor.when(AssignNode)
    def visit(self, node, scope):
        print('assign')        
        var = self.find_var(node.id, scope)
        if var is None:    
            self.errors.append(VARIABLE_NOT_DEFINED % (node.id, self.current_method.name))
            var_type = ErrorType()
        else:
            var_type = var.type
        
        expr_type = self.visit(node.expr, scope)
        if not var_type.conforms_to(expr_type):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, var_type.name))
        
        return expr_type

    @visitor.when(CallNode)
    def visit(self, node, scope):
        print('call')
        if node.ancestor_type is None:
            #if obj is id
            if node.obj == 'SELF_TYPE':
                obj_type = self.current_type
            else:
                obj_type = self.visit(node.obj, scope)
        else:
            # print('ancestor exists')
            obj_type = Context.get_type(node.ancestor_type)
            # print(obj_type)

            
        try:
            method = obj_type.get_method(node.id)
        except SemanticError as error:
            self.errors.append(error.text)
            return ErrorType()

        if not len(method.param_names) == len(node.args):
            self.errors.append(METHOD_ARGS_UNMATCH % (method.name))
        else:
            for i in range(0, len(node.args)):
                arg_type = self.visit(node.args[i], scope)
                if not method.param_types[i].conforms_to(arg_type):
                    self.errors.append(INCOMPATIBLE_TYPES % (arg_type.name, method.param_types[i].name))
        return method.return_type
            
    @visitor.when(ArithBinaryNode)
    def visit(self, node, scope):
        print('arith binary')
        left_type = self.visit(node.left, scope)
        right_type = self.visit(node.right, scope)
        int_type = IntType()
        print('left',left_type)
        print('right',right_type)
        if not left_type.name == int_type.name or not right_type.name == int_type.name:
            self.errors.append(INVALID_OPERATION % (left_type.name, right_type.name))
        return int_type
        
    @visitor.when(BooleanBinaryNode)
    def visit(self, node, scope):
        print('boolean binary')
        left_type = self.visit(node.left, scope)
        right_type = self.visit(node.right, scope)
        int_type = IntType()
        if not left_type.name == int_type.name or not right_type.name == int_type.name:
            self.errors.append(INVALID_OPERATION % (left_type.name, right_type.name))
        return BoolType()

    @visitor.when(ConstantNumNode)
    def visit(self, node, scope):
        print('constant')
        return IntType()

    @visitor.when(BoolNode)
    def visit(self, node, scope):
        print('bool')
        return BoolType()

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        print('variable')
        
        var = self.find_var(node.lex, scope)
        if var is None:
            self.errors.append(VARIABLE_NOT_DEFINED%(node.lex,self.current_method.name))
            return ErrorType()
        else:
            var_type = var.type
            return var_type

    @visitor.when(InstantiateNode)
    def visit(self, node, scope):
        print('instantiate')
        try:
            instance_type = self.context.get_type(node.lex)
        except SemanticError as error:
            self.errors.append(error.text)
            instance_type = ErrorType()
        return instance_type
    
    @visitor.when(NotNode)
    def visit(self, node, scope):
        print('not node')
        expr_type = self.visit(node.expr, scope)
        if (expr_type.name != BoolType().name):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, BoolType().name))
        return BoolType()

    @visitor.when(IsVoidNode)
    def visit(self, node, scope):
        print('is void')
        expr_type = self.visit(node.expr, scope)
        if (expr_type.name != VoidType().name):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, VoidType().name))
        return BoolType()

    @visitor.when(TildeNode)
    def visit(self, node, scope):
        print('tilde')
        expr_type = self.visit(node.expr, scope)
        if (expr_type.name != IntType().name):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, IntType().name))
        
        return IntType()

    @visitor.when(VariableNode)
    def visit(self, node, scope):
        print('variable')
        
        var = self.find_var(node.lex, scope)
        if var is None:
            self.errors.append(VARIABLE_NOT_DEFINED%(node.lex,self.current_method.name))
            return ErrorType()
        else:
            var_type = var.type
            return var_type



    def find_var(self, vname, scope):
        s = scope
        while s is not None:
            for local in s.locals:
                if local.name == vname:
                    return local
            s = s.parent
        return None