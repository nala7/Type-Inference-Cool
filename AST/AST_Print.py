import cmp.visitor as visitor
from AST.AST_Hierarchy import *


class FormatVisitor(object):
    @visitor.on("node")
    def visit(self, node, tabs):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__ProgramNode [<class> ... <class>]"
        statements = "\n".join(
            self.visit(child, tabs + 1) for child in node.declarations
        )
        return f"{ans}\n{statements}"

    @visitor.when(ClassDeclarationNode)
    def visit(self, node, tabs=0):
        parent = "" if node.parent is None else f": {node.parent}"
        ans = (
            "\t" * tabs
            + f"\\__ClassDeclarationNode: class {node.id} {parent} {{ <feature> ... <feature> }}"
        )
        features = "\n".join(self.visit(child, tabs + 1) for child in node.features)
        return f"{ans}\n{features}"

    @visitor.when(FuncDeclarationNode)
    def visit(self, node, tabs=0):
        params = ", ".join(":".join(param) for param in node.params)
        ans = (
            "\t" * tabs
            + f"\\__FuncDeclarationNode: def {node.id}({params}) : {node.type} -> <body>"
        )
        body = self.visit(node.body, tabs + 1)
        return f"{ans}\n{body}"

    @visitor.when(AttrDeclarationNode)
    def visit(self, node, tabs=0):
        ans = (
            "\t" * tabs + f"\\__AttrDeclarationNode: {node.id} : {node.type} <- <value>"
        )
        if node.val is None:
            return f"{ans}"
        value = self.visit(node.val, tabs + 1)
        return f"{ans}\n{value}"

    @visitor.when(ConditionalNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__ConditionalNode: if <expr> then <expr> else <expr>"
        if_expr = self.visit(node.if_expr, tabs + 1)
        then_expr = self.visit(node.then_expr, tabs + 1)
        else_expr = self.visit(node.else_expr, tabs + 1)
        return f"{ans}\n{if_expr}\n{then_expr}\n{else_expr}"

    @visitor.when(LoopNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__LoopNode: while <condition> -> <body>"
        condition = self.visit(node.condition, tabs + 1)
        body = self.visit(node.body, tabs + 1)
        return f"{ans}\n{condition}\n{body}"

    @visitor.when(BlockNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + "\\__BlockNode: { <expr_list> }"
        for child in node.expr_list:
            ans += "\n" + self.visit(child, tabs + 1)
        return f"{ans}"

    @visitor.when(LetNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__LetNode: let <vars> in <body>"
        params = "\t" * (tabs + 1) + f"\\__vars:"
        for child in node.var_list:
            params += (
                "\n"
                + "\t" * (tabs + 2)
                + f"\\__{str(child[0])} : {str(child[1])} <- <value>"
            )
            if child[2] is not None:
                params += "\n" + self.visit(child[2], tabs + 3)
        body = self.visit(node.body, tabs + 1)
        return f"{ans}\n{params}\n{body}"

    @visitor.when(CaseNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__CaseNode: case <expr> of <branch_list> esac"
        expr = self.visit(node.expr, tabs + 1)
        branches = ""
        for branch in node.branch_list:
            branch_head = (
                "\n"
                + "\t" * (tabs + 1)
                + f"\\__{str(branch[0])} : {str(branch[1])} => <expr>"
            )
            branch_expr = self.visit(branch[2], tabs + 2)
            branches += f"{branch_head}\n{branch_expr}"
        return f"{ans}\n{expr}{branches}"

    @visitor.when(AssignNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__AssignNode: {node.id} <- <expr>"
        expr = self.visit(node.expr, tabs + 1)
        return f"{ans}\n{expr}"

    @visitor.when(CallNode)
    def visit(self, node, tabs=0):
        ans = (
            "\t" * tabs
            + f"\\__CallNode: <obj>.{node.id}@{node.ancestor_type}(<expr>, ..., <expr>)"
        )
        obj = self.visit(node.obj, tabs + 1)
        args = "\n".join(self.visit(arg, tabs + 1) for arg in node.args)
        return f"{ans}\n{obj}\n{args}"

    @visitor.when(BinaryNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__<expr> {node.__class__.__name__} <expr>"
        left = self.visit(node.left, tabs + 1)
        right = self.visit(node.right, tabs + 1)
        return f"{ans}\n{left}\n{right}"

    @visitor.when(AtomicNode)
    def visit(self, node, tabs=0):
        return "\t" * tabs + f"\\__ {node.__class__.__name__}: {node.lex}"

    @visitor.when(InstantiateNode)
    def visit(self, node, tabs=0):
        return "\t" * tabs + f"\\__ InstantiateNode: new {node.lex}()"

    @visitor.when(NotNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__ NotNode: not <expr>"
        expr = self.visit(node.expr, tabs + 1)
        return f"{ans}\n{expr}"

    @visitor.when(IsVoidNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__ IsVoidNode: not <expr>"
        expr = self.visit(node.expr, tabs + 1)
        return f"{ans}\n{expr}"

    @visitor.when(TildeNode)
    def visit(self, node, tabs=0):
        ans = "\t" * tabs + f"\\__ TildeNode: not <expr>"
        expr = self.visit(node.expr, tabs + 1)
        return f"{ans}\n{expr}"
