import cmp.visitor as visitor
from cmp.semantic import Scope, SelfType
from cmp.semantic import SemanticError
from cmp.semantic import Attribute, Method, Type, AutoType
from cmp.semantic import VoidType, ErrorType, IntType, BoolType, ObjType
from cmp.semantic import Context
from AST.AST_Hierarchy import *

VAR_AUTOTYPE = 'Variable "%s" type not infered in "%s".'
METH_AUTOTYPE = 'Method "%s" return type not infered in "%s"'
WRONG_SIGNATURE = 'Method "%s" already defined in "%s" with a different signature.'
SELF_IS_READONLY = 'Variable "self" is read-only.'
LOCAL_ALREADY_DEFINED = 'Variable "%s" is already defined in method "%s".'
ATTR_ALREADY_DEFINED = 'Attribute "%s" is already defined in ancestor class.'
INCOMPATIBLE_TYPES = 'Cannot convert "%s" into "%s".'
VARIABLE_NOT_DEFINED = 'Variable "%s" is not defined in "%s".'
INVALID_OPERATION = 'Operation is not defined between "%s" and "%s".'
METHOD_ARGS_UNMATCH = 'Method "%s" arguments do not match with definition.'


class TypeInferer:
    def __init__(self, context, errors=[], autotypes = []):
        self.context = context
        self.current_type = None
        self.current_method = None
        self.errors = errors
        self.autotypes = autotypes
    
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

    @visitor.when(ConditionalNode)
    def visit(self, node, scope):
        print('conditional')
        cond_type = self.visit(node.if_expr, scope)
        if not cond_type.conforms_to(BoolType()):
            self.errors.append(INCOMPATIBLE_TYPES % (cond_type.name, BoolType().name))

        then_expr_type = self.visit(node.then_expr, scope)
        else_expr_type = self.visit(node.else_expr, scope)
        
        common_ancestor_type = self.context.find_first_common_ancestor(then_expr_type, else_expr_type)

        return common_ancestor_type
            
    @visitor.when(LoopNode)
    def visit(self, node, scope):
        print('loop')
        
        cond_type = self.visit(node.condition, scope)
        if not cond_type.conforms_to(BoolType()):
            self.errors.append(INCOMPATIBLE_TYPES % (cond_type.name, BoolType().name))
        
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
            var_type = self.context.get_type(typex)

            if expr is not None:
                expr_type = self.visit(expr, child_scope)
                if var_type.name == AutoType().name:
                    var_type = expr_type
                    if expr_type.name == AutoType().name:
                        self.autotypes.append(VAR_AUTOTYPE%(var, self.current_type.name))             
            else:
                expr_type = var_type

            if not var_type.conforms_to(expr_type):
                self.errors.append(INCOMPATIBLE_TYPES % (var_type.name, expr_type.name))

            child_scope.define_variable(var, var_type)

        return self.visit(node.body, child_scope)

    @visitor.when(CaseNode)
    def visit(self, node, scope):
        print('case')
        self.visit(node.expr, scope)

        return_type = None
        child_scope = scope.create_child()
        for var, typex, expr in node.branch_list:
            var_type = self.context.get_type(typex)
            
            child_scope = child_scope.create_child()
            expr_type = self.visit(expr, child_scope)
            if not var_type.conforms_to(expr_type):
                self.errors.append(INCOMPATIBLE_TYPES % (var_type.name, expr_type.name))
                
            if var_type.name == AutoType().name:
                var_type = expr_type
                if expr_type.name == AutoType().name:
                    self.autotypes.append(VAR_AUTOTYPE%(var, self.current_type.name))    

            if return_type is None:
                return_type = var_type          

            return_type = self.context.find_first_common_ancestor(var_type, return_type)

            scope.define_variable(var, var_type)
        return return_type

    @visitor.when(AssignNode)
    def visit(self, node, scope):
        print('assign')        
        var = self.find_var(node.id, scope)
        
        expr_type = self.visit(node.expr, scope)
        
        if var.type.name == AutoType().name:
            var.type = expr_type
            if expr_type.name == AutoType().name:
                self.autotypes.append(VAR_AUTOTYPE%(var.name, self.current_type.name))    

        if not var.type.conforms_to(expr_type):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, var.type.name))
        
        return expr_type

    @visitor.when(CallNode)
    def visit(self, node, scope):
        print('call')
        if node.ancestor_type is None:
            #if obj is id
            if node.obj == 'self':
                obj_type = self.current_type
            else:
                obj_type = self.visit(node.obj, scope)
                if obj_type.name == AutoType().name:
                    self.errors.append('Method '+id+' not callable')
        else:
            # print('ancestor exists')
            obj_type = Context.get_type(node.ancestor_type)
            # print(obj_type)

            
        try:
            method = obj_type.get_method(node.id)
        except SemanticError as error:
            self.errors.append(error.text)
            return ErrorType()

        for i in range(0, len(node.args)):
            arg_type = self.visit(node.args[i], scope)
            param_type = method.param_types[i]
            if param_type.name == AutoType().name:
                method.param_types[i] = arg_type
                if arg_type.name == AutoType().name:
                    self.autotypes.append(VAR_AUTOTYPE%(method.param_name[i], method.name)) 

            if not method.param_types[i].conforms_to(arg_type):
                self.errors.append(INCOMPATIBLE_TYPES % (arg_type.name, method.param_types[i].name))
        return method.return_type
            
    @visitor.when(ArithBinaryNode)
    def visit(self, node, scope):
        print('arith binary')
        left_type = self.visit(node.left, scope)
        right_type = self.visit(node.right, scope)
        int_type = IntType()
        if not left_type.conforms_to(int_type) or not right_type.conforms_to(int_type):
            self.errors.append(INVALID_OPERATION % (left_type.name, right_type.name))
        return int_type
        
    @visitor.when(BooleanBinaryNode)
    def visit(self, node, scope):
        print('boolean binary')
        left_type = self.visit(node.left, scope)
        right_type = self.visit(node.right, scope)
        int_type = IntType()
        if not left_type.conforms_to(int_type) or not right_type.conforms_to(int_type):
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
        var_type = var.type
        return var_type

    @visitor.when(InstantiateNode)
    def visit(self, node, scope):
        print('instantiate')
        instance_type = self.context.get_type(node.lex)

        return instance_type
    
    @visitor.when(NotNode)
    def visit(self, node, scope):
        print('not node')
        expr_type = self.visit(node.expr, scope)
        if not expr_type.conforms_to(BoolType()):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, BoolType().name))
        return BoolType()

    @visitor.when(IsVoidNode)
    def visit(self, node, scope):
        print('is void')
        self.visit(node.expr, scope)
        return BoolType()

    @visitor.when(TildeNode)
    def visit(self, node, scope):
        print('tilde')
        expr_type = self.visit(node.expr, scope)
        if expr_type.conforms_to(IntType()):
            self.errors.append(INCOMPATIBLE_TYPES % (expr_type.name, IntType().name))
        return IntType()

    def find_var(self, vname, scope):
        s = scope
        while s is not None:
            for local in s.locals:
                if local.name == vname:
                    return local
            s = s.parent
        return None