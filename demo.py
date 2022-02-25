from src.veda.ast_printer import AstPrinter
from src.veda.token import Token
from src.veda.token_type import TokenType
from src.veda.expr import Binary, Unary, Literal, Grouping

# (-213) * (45.67)
expression = Binary(
    Unary(
        Token(TokenType.MINUS, "-", None, 1), 
        Literal(123)
    ), 
    Token(TokenType.STAR, "*", None, 1),
    Grouping(Literal(45.67))
)
print(AstPrinter().print(expression))