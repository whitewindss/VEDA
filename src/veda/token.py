from typing import Optional
from .token_type import TokenType

class Token:
    type: TokenType
    lexeme: str
    literal: object
    line: int

    def __init__(self, type: TokenType, lexeme: str, literal: Optional[object], line: int) -> None:
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self) -> str:
        return f"<{self.type:21}, {self.lexeme}, {self.literal}>"

    def __repr__(self) -> str:
        return str(self)

