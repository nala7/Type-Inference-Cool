import cmp.visitor as visitor
from AST.AST_Hierarchy import *

class FormatVisitor(object):
    @visitor.on('node')
    def visit(self, node, tabs):
        pass
    
    @visitor.when(ProgramNode)
    def visit(self, node, tabs=0):
        print('prog node')
        ans = '\t' * tabs + f'\\__ProgramNode [<class> ... <class>]'
        statements = '\n'.join(self.visit(child, tabs + 1) for child in node.declarations)
        return f'{ans}\n{statements}'
    
    @visitor.when(ClassDeclarationNode)
    def visit(self, node, tabs=0):
        parent = '' if node.parent is None else f": {node.parent}"
        ans = '\t' * tabs + f'\\__ClassDeclarationNode: class {node.id} {parent} {{ <feature> ... <feature> }}'
        features = '\n'.join(self.visit(child, tabs + 1) for child in node.features)
        return f'{ans}\n{features}'

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, tabs=0):
        params = ', '.join(':'.join(param) for param in node.params)
        ans = '\t' * tabs + f'\\__FuncDeclarationNode: def {node.id}({params}) : {node.type} -> <body>'
        body = self.visit(node.body, tabs + 1)
        return f'{ans}\n{body}'
    
    @visitor.when(AttrDeclarationNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AttrDeclarationNode: {node.id} : {node.type}  -> <value>'
        value = self.visit(node.val, tabs + 1)
        return f'{ans}\n{value}'

    @visitor.when(ConditionalNode)
    def visit(self, node, tabs=0):
        if_expr = self.visit(node.if_expr)
        then_expr = self.visit(node.then_expr)
        else_expr = self.visit(node.else_expr)
        ans =  '\t' * tabs + f'\\__ConditionalNode: if {if_expr} then {then_expr} else {else_expr}'
        return f'{ans}'

    @visitor.when(LoopNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__LoopNode: while {node.condition} -> <body>'
        body = self.visit(node.body, tabs + 1)
        return f'{ans}\n{body}'

    @visitor.when(BlockNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + '\\__BlockNode: {'
        ans += '\n'.join(self.visit(child, tabs + 1) for child in node.expr_list)
        ans += ' }'
        return f'{ans}'
        
    @visitor.when(LetNode)
    def visit(self, node, tabs=0):
        params = ', '.join(self.visit(child) for child in node.var_list)
        body = self.visit(node.body, tabs + 1)
        ans = '\t' * tabs + f'\\__LetNode: let {params} in {body}'
        return f'{ans}'

    @visitor.when(CaseNode)
    def visit(self, node, tabs={0}):
        expr = self.visit(node.expr)
        branches = '\n'.join(self.visit(branch, tabs + 1) for branch in node.branch_list)
        ans = '\t' * tabs + f'\\__CaseNode: case {expr} of {branches} esac'
        return f'{ans}'

    @visitor.when(AssignNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__AssignNode: let {node.id} = <expr>'
        expr = self.visit(node.expr, tabs + 1)
        return f'{ans}\n{expr}'

    @visitor.when(CallNode)
    def visit(self, node, tabs=0):
        obj = self.visit(node.obj, tabs + 1)
        ans = '\t' * tabs + f'\\__CallNode: <obj>.{node.id}:{node.ancestor}(<expr>, ..., <expr>)'
        args = '\n'.join(self.visit(arg, tabs + 1) for arg in node.args)
        return f'{ans}\n{obj}\n{args}'

    @visitor.when(BinaryNode)
    def visit(self, node, tabs=0):
        ans = '\t' * tabs + f'\\__<expr> {node.__class__.__name__} <expr>'
        left = self.visit(node.left, tabs + 1)
        right = self.visit(node.right, tabs + 1)
        return f'{ans}\n{left}\n{right}'

    @visitor.when(AtomicNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__ {node.__class__.__name__}: {node.lex}'
    
    @visitor.when(InstantiateNode)
    def visit(self, node, tabs=0):
        return '\t' * tabs + f'\\__ InstantiateNode: new {node.lex}()'