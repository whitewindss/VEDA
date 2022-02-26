import sys
from typing import List

from .ast_printer import AstPrinter
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
    def error_token(cls, token: Token, message: str):
        if token.type == TokenType.EOF:
            cls.report(token.line, " at end", message)
        else:
            cls.report(token.line, f"at '{token.lexeme}'", message)

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
            print("> ", end="")
            line = input()
            if line is None:
                break
            self.__run(line)
            self.had_error = False

    def __run(self, source: str):
        from .parser import Parser
        from .scanner import Scanner

        tokens = Scanner(source).scan_tokens()  # type: List[Token]

        expression = Parser(tokens).parse()
        if self.had_error:
            return
        if not expression:
            return
        print(AstPrinter().print(expression))
