import sys
from typing import List

from .token import Token
from .token_type import TokenType


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
                break
            self.__run(line)
            self.had_error = False

    def __run(self, source: str):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()  # type: List[Token]
        for token in tokens:
            print(token)


class Scanner:
    keywords = {
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
        "while": TokenType.WHILE,
    }

    def __init__(self, source: str):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = list()  # type: List[Token]

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        if c == "(":
            self.add_token(TokenType.LEFT_PAREN)
        elif c == ")":
            self.add_token(TokenType.RIGHT_PAREN)
        elif c == "{":
            self.add_token(TokenType.LEFT_BRACE)
        elif c == "}":
            self.add_token(TokenType.RIGHT_BRACE)
        elif c == ",":
            self.add_token(TokenType.COMMA)
        elif c == ".":
            self.add_token(TokenType.DOT)
        elif c == "-":
            self.add_token(TokenType.MINUS)
        elif c == "+":
            self.add_token(TokenType.PLUS)
        elif c == ";":
            self.add_token(TokenType.SEMICOLON)
        elif c == "*":
            self.add_token(TokenType.STAR)
        elif c == "!":
            self.add_token(TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG)
        elif c == "=":
            self.add_token(TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL)
        elif c == "<":
            self.add_token(TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS)
        elif c == ">":
            self.add_token(TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER)
        elif c == "/":
            if self.match("/"):
                while self.peek() != "\n" and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)
        elif c in (" ", "\r", "\t"):
            return
        elif c == "\n":
            self.line += 1
        elif c == '"':
            self.string()
        else:
            if self.is_digit(c):
                self.number()

            elif self.is_alpha(c):
                self.identifier()
            else:
                Veda.error(self.line, "Unexpected character.")

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()

        text = self.source[self.start : self.current]
        type = self.keywords.get(text, TokenType.IDENTIFIER)
        self.add_token(type)

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == "." and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()

        self.add_token_literal(TokenType.NUMBER, float(self.source[self.start : self.current]))

    def string(self):
        while (self.peek() != '"') and (not self.is_at_end()):
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.is_at_end():
            Veda.error(self.line, "Unterminated string.")
            return

        self.advance()

        value = self.source[self.start + 1 : self.current - 1]
        self.add_token_literal(TokenType.STRING, value)

    def match(self, expected: str):
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self):
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def peek_next(self):
        if (self.current + 1) >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def is_alpha(self, c: str) -> bool:
        return ("a" <= c <= "z") or ("A" <= c <= "Z") or (c == "_")

    def is_alpha_numeric(self, c: str):
        return self.is_alpha(c) or self.is_digit(c)

    def is_digit(self, c: str):
        return "0" <= c <= "9"

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def add_token(self, type: TokenType):
        self.add_token_literal(type, None)

    def add_token_literal(self, type: TokenType, literal: object):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type, text, literal, self.line))
