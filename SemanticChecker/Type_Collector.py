import cmp.nbpackage
import cmp.visitor as visitor
from AST.AST_Hierarchy import *
from cmp.semantic import ObjType, SemanticError
from cmp.semantic import Attribute, Method, Type
from cmp.semantic import VoidType, ErrorType
from cmp.semantic import IntType, StrType, SelfType, AutoType, BoolType
from cmp.semantic import Context

class TypeCollector(object):
    def __init__(self, errors=[]):
        self.context = None
        self.errors = errors
    
    @visitor.on('node')
    def visit(self, node):
        pass
    
    @visitor.when(ProgramNode)
    def visit(self, node):
        self.context = Context()

        bool_type = BoolType()
        
        int_type = IntType()

        str_type = StrType()
        str_type.define_method('length', [], [], int_type)
        str_type.define_method('concat', ['s'], ['String'], str_type)
        str_type.define_method('substr', ['i','l'], ['Int','Int'], str_type)
        
        obj_type = ObjType()
        obj_type.define_method('abort', [], [], obj_type)
        obj_type.define_method('type_name', [], [], str_type)
        obj_type.define_method('copy', [], [], SelfType())

        io_type = self.context.create_type('IO')
        io_type.define_method('out_string', ['x'], ['String'], SelfType())
        io_type.define_method('out_int', ['x'], ['Int'], SelfType())
        io_type.define_method('in_string', [], [], str_type)
        io_type.define_method('in_int', [], [], int_type)
        io_type.set_parent(obj_type)

        self.context.types['Bool'] = bool_type
        bool_type.set_parent(obj_type)
        self.context.types['Int'] = int_type
        int_type.set_parent(obj_type)
        self.context.types['String'] = str_type
        str_type.set_parent(obj_type)
        self.context.types['Object'] = obj_type
        self.context.types['<error>'] = ErrorType()
        self.context.types['<error>'].set_parent(obj_type)
        self.context.types['Void'] = VoidType()
        self.context.types['Void'].set_parent(obj_type)
        self.context.types['SELF_TYPE'] = SelfType()
        self.context.types['SELF_TYPE'].set_parent(obj_type)
        self.context.types['AUTO_TYPE'] = AutoType()
        self.context.types['AUTO_TYPE'].set_parent(obj_type)

        for class_dec_node in node.declarations:
            self.visit(class_dec_node)
        
    @visitor.when(ClassDeclarationNode)
    def visit(self, node):
        try:
            typex = self.context.create_type(node.id)
            typex.set_parent(self.context.types['Object'])
        except SemanticError as error:
            self.errors.append(error.text)
