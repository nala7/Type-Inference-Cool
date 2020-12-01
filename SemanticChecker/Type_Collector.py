import cmp.nbpackage
import cmp.visitor as visitor
from AST.AST_Hierarchy import *
from cmp.semantic import SemanticError
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
        self.context.types['<error>'] = ErrorType()
        self.context.types['<void>'] = VoidType()
        self.context.types['int'] = IntType()
        self.context.types['str'] = StrType()
        self.context.types['bool'] = BoolType()
        self.context.types['SELF_TYPE'] = SelfType()
        self.context.types['AUTO_TYPE'] = AutoType()
        for class_dec_node in node.declarations:
            self.visit(class_dec_node)
        
    @visitor.when(ClassDeclarationNode)
    def visit(self, node):
        try:
            self.context.create_type(node.id)
        except SemanticError as error:
            self.errors.append(error.text)
