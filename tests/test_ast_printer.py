from src.veda.ast_printer import AstPrinter
from src.veda.expr import Binary, Grouping, Literal, Unary
from src.veda.token import Token
from src.veda.token_type import TokenType


def test_simple_expression():
    # (-213) * (45.67)
    expression = Binary(
        Unary(Token(TokenType.MINUS, "-", None, 1), Literal(123)),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(Literal(45.67)),
    )
    assert AstPrinter().print(expression) == "(* (- 123) (group 45.67))"
