from typing import List

from .expr import Binary, Expr, Grouping, Literal, Unary


class AstPrinter:
    def print(self, expr: Expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr: Binary):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping_expr(self, expr: Grouping):
        return self.parenthesize("group", expr.expression)

    def visit_literal_expr(self, expr: Literal):
        if expr.value is None:
            return "nil"
        return str(expr.value)

    def visit_unary_expr(self, expr: Unary):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name: str, *exprs: Expr):
        buffer = list()  # type: List[str]
        buffer.append("(")
        buffer.append(name)
        for expr in exprs:
            buffer.append(" ")
            buffer.append(expr.accept(self))
        buffer.append(")")

        return "".join(buffer)
