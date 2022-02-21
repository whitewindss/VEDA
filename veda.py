import sys
from typing import List, Optional
from enum import Enum

class TokenType(Enum):
    # Single-character tokens.
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    LEFT_BRACE = 3
    RIGHT_BRACE = 4
    COMMA = 5
    DOT = 6
    MINUS = 7
    PLUS = 8
    SEMICOLON = 9
    SLASH = 10
    STAR = 11

    # One or two character tokens.
    BANG = 12
    BANG_EQUAL = 13
    EQUAL = 14
    EQUAL_EQUAL = 15
    GREATER = 16
    GREATER_EQUAL = 17
    LESS = 18 
    LESS_EQUAL = 19

    # Literals.
    IDENTIFIER = 20
    STRING = 21
    NUMBER = 22

    # Keywords.
    AND = 23 
    CLASS = 24
    ELSE = 25
    FALSE = 26 
    FUN = 27 
    FOR = 28
    IF = 29 
    NIL = 30
    OR = 31
    PRINT = 32
    RETURN = 33
    SUPER = 34
    THIS = 35
    TRUE = 36
    VAR = 37
    WHILE = 38

    EOF = 39


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


class Scanner:
    __tokens: List[Token] = list()
    __start = 0
    __current = 0
    __line = 0
    __keywords = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "fun": TokenType.FUN,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE
    }

    def __init__(self, source: str) -> None:
        self.source = source

    def scan_tokens(self) -> List[Token]:
        while not self.__is_at_end:
            # 
            self.__start = self.__current
            self.__scan_token()

        self.__tokens.append(Token(TokenType.EOF, "", None, self.__line))
        return self.__tokens

    def __scan_token(self):
        c = self.__advance()
        if c == "(":
            self.__add_token(TokenType.LEFT_PAREN)
        elif c == ")":
            self.__add_token(TokenType.RIGHT_PAREN)
        elif c == "{":
            self.__add_token(TokenType.LEFT_BRACE)
        elif c == "}":
            self.__add_token(TokenType.RIGHT_BRACE)
        elif c == ",":
            self.__add_token(TokenType.COMMA)
        elif c == ".":
            self.__add_token(TokenType.DOT)
        elif c == "-":
            self.__add_token(TokenType.MINUS)
        elif c == "+":
            self.__add_token(TokenType.PLUS)
        elif c == ";":
            self.__add_token(TokenType.SEMICOLON)
        elif c == "*":
            self.__add_token(TokenType.STAR)
        elif c == "!":
            self.__add_token(TokenType.BANG_EQUAL if self.__match("=") else TokenType.BANG)
        elif c == "=":
            self.__add_token(TokenType.EQUAL_EQUAL if self.__match("=") else TokenType.EQUAL)
        elif c == "<":
            self.__add_token(TokenType.LESS_EQUAL if self.__match("=") else TokenType.LESS)
        elif c == ">":
            self.__add_token(TokenType.GREATER_EQUAL if self.__match("=") else TokenType.GREATER)
        elif c == "/":
            if self.__match("/"):
                while self.__peek() != "\n" and self.__is_at_end:
                    self.__advance()
            else:
                self.__add_token(TokenType.SLASH)
        elif c in (" ", "\r", "\t"):
            pass
        elif c == "\n":
            self.__line += 1
        elif c == "\"":
            self.__string()
        elif c == "\0":
            return
        else:
            if self.__is_digit(c):
                self.__number()
            elif self.__is_alpha(c):
                self.__identifier()
            else:
                Veda.error(self.__line, f"Unexpected character: {c}")

    def __is_alpha(self, c: str):
        return ("a" <= c <= "z") or ("A" <= c <= "Z") or (c == "_")
    
    def __identifier(self):
        while self.__is_alpha_numeric(self.__peek()):
            self.__advance()
        text = self.source[self.__start: self.__current]
        type = self.__keywords.get(text, TokenType.IDENTIFIER)

        self.__add_token(type)

    def __is_alpha_numeric(self, c: str):
        return self.__is_alpha(c) or self.__is_digit(c)

    def __is_digit(self, c: str):
        return "0" <= c <= "9"

    def __number(self):
        while self.__is_digit(self.__peek()):
            self.__advance()
        
        if self.__peek() == "." and self.__is_digit(self.__peek_next()):
            self.__advance()

            while self.__is_digit(self.__peek()):
                self.__advance()

        self.__add_token_object(TokenType.NUMBER, float(self.source[self.__start: self.__current]))

    def __peek_next(self):
        if (self.__current + 1 >= len(self.source)):
            return "\0"
        return self.source[self.__current + 1]

    def __string(self):
        while self.__peek() != "\""  and not self.__is_at_end:
            if self.__peek() == "\n":
                self.__line += 1
                self.__advance()
        if self.__is_at_end:
            Veda.error(self.__line, "Unterminated string.")
            return

        self.__advance()

        value = self.source[self.__start + 1: self.__current - 1]
        self.__add_token_object(TokenType.STRING, value)

    def __peek(self):
        if self.__is_at_end:
            return "\0"

        return self.source[self.__current]

    def __match(self, expected: str):
        if self.__is_at_end:
            return False
        if self.source[self.__current] != expected:
            return False
        self.__current += 1
        return True

    def __advance(self) -> str:
        self.__current += 1
        if self.__is_at_end:
            return "\0"
        return self.source[self.__current]

    def __add_token(self, token: TokenType):
        self.__add_token_object(token)

    def __add_token_object(self, type: TokenType, literal: Optional[object]=None):
        text = self.source[self.__start: self.__current]
        self.__tokens.append(Token(type, text, literal, self.__line))


    @property
    def __is_at_end(self):
        return self.__current >= len(self.source)
        


class Veda:
    had_error = False

    def main(self, *args: str):
        if len(args) > 1:
            print("Usage: veda [script]")
            sys.exit(64)
        elif len(args) == 1:
            self.__run_file(args[0])
        else:
            self.__run_prompt()

    @classmethod
    def error(cls, line: int, message: str):
        cls.report(line, "", message)

    @classmethod
    def report(cls, line: int, where: str, message: str):
        print(f"[line: {line}] Error {where}: {message}")
        cls.had_error = True

    def __run_file(self, path: str):
        _file = None
        with open(path) as f:
            _file = f.read()
        self.__run(_file)
        if self.had_error:
            sys.exit(65)
    
    def __run_prompt(self):
        while True:
            print("> ")
            line = input()
            if line is None:
                break;
            self.__run(line)
            self.had_error = False

    
    def __run(self, source: str):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()  # type: List[Token]
        for token in tokens:
            print(token)

source = """
var veda = 1;

veda = veda + 1.9;
veda >= 4.8;
(veda >= 4.8) and (veda < 8.9);
"""
if __name__ == "__main__":
    tokens = Scanner(source).scan_tokens()
    print("\n".join([str(t) for t in tokens]))
