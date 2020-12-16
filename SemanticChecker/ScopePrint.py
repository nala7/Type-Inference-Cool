from cmp.semantic import Scope


class ScopePrint:
    def visit(self, scope: Scope, tabs=0):
        ans = "\t" * tabs + f"\\__ID:{scope.id}, VARS:"
        for var_info in scope.locals:
            ans += f" ({var_info.name},{var_info.type.name})"

        children = "\n".join(self.visit(child, tabs + 1) for child in scope.children)

        if len(scope.children) == 0:
            return f"{ans}"
        return f"{ans}\n{children}"
