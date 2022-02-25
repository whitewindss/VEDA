import pytest

from src.veda import Scanner, Token, TokenType


def _token_equal(a: Token, b: Token):
    return all([a.type == b.type, a.lexeme == b.lexeme, a.literal == b.literal])


TOKEN_EOF = Token(type=TokenType.EOF, lexeme="", literal=None, line=0)

TOKEN_LEFT_PAREN = Token(type=TokenType.LEFT_PAREN, lexeme="(", literal=None, line=0)

TOKEN_RIGHT_PAREN = Token(type=TokenType.RIGHT_PAREN, lexeme=")", literal=None, line=0)

TOKEN_LEFT_BRACE = Token(type=TokenType.LEFT_BRACE, lexeme="{", literal=None, line=0)

TOKEN_RIGHT_BRACE = Token(type=TokenType.RIGHT_BRACE, lexeme="}", literal=None, line=0)

TOKEN_COMMA = Token(type=TokenType.COMMA, lexeme=",", literal=None, line=0)

TOKEN_DOT = Token(type=TokenType.DOT, lexeme=".", literal=None, line=0)

TOKEN_MINUS = Token(type=TokenType.MINUS, lexeme="-", literal=None, line=0)

TOKEN_PLUS = Token(type=TokenType.PLUS, lexeme="+", literal=None, line=0)

TOKEN_SEMICOLON = Token(type=TokenType.SEMICOLON, lexeme=";", literal=None, line=0)

TOKEN_SLASH = Token(type=TokenType.SLASH, lexeme="/", literal=None, line=0)

TOKEN_STAR = Token(type=TokenType.STAR, lexeme="*", literal=None, line=0)

TOKEN_BANG = Token(TokenType.BANG, "!", None, 0)

TOKEN_BANG_EQUAL = Token(TokenType.BANG_EQUAL, "!=", None, 0)

TOKEN_EQUAL = Token(TokenType.EQUAL, "=", None, 0)

TOKEN_EQUAL_EQUAL = Token(TokenType.EQUAL_EQUAL, "==", None, 0)

TOKEN_GREATER = Token(TokenType.GREATER, ">", None, 0)

TOKEN_GREATER_EQUAL = Token(TokenType.GREATER_EQUAL, ">=", None, 0)

TOKEN_LESS = Token(TokenType.LESS, "<", None, 0)

TOKEN_LESS_EQUAL = Token(TokenType.LESS_EQUAL, "<=", None, 0)

TOKEN_AND = Token(TokenType.AND, "and", None, 0)

TOKEN_CLASS = Token(TokenType.CLASS, "class", None, 0)

TOKEN_ELSE = Token(TokenType.ELSE, "else", None, 0)

TOKEN_FALSE = Token(TokenType.FALSE, "false", None, 0)

TOKEN_FUN = Token(TokenType.FUN, "fun", None, 0)

TOKEN_FOR = Token(TokenType.FOR, "for", None, 0)

TOKEN_IF = Token(TokenType.IF, "if", None, 0)

TOKEN_NIL = Token(TokenType.NIL, "nil", None, 0)

TOKEN_OR = Token(TokenType.OR, "or", None, 0)

TOKEN_PRINT = Token(TokenType.PRINT, "print", None, 0)

TOKEN_RETURN = Token(TokenType.RETURN, "return", None, 0)

TOKEN_SUPER = Token(TokenType.SUPER, "super", None, 0)

TOKEN_THIS = Token(TokenType.THIS, "this", None, 0)

TOKEN_TRUE = Token(TokenType.TRUE, "true", None, 0)

TOKEN_VAR = Token(TokenType.VAR, "var", None, 0)

TOKEN_WHILE = Token(TokenType.WHILE, "while", None, 0)


def test_scan_empty_string():
    tokens = Scanner("").scan_tokens()
    assert all([len(tokens) == 1, _token_equal(tokens[0], TOKEN_EOF)])


def test_scan_left_paren():
    tokens = Scanner("(").scan_tokens()
    assert all([len(tokens) == 2, _token_equal(tokens[0], TOKEN_LEFT_PAREN)])


def test_scan_right_paren():
    tokens = Scanner(")").scan_tokens()
    assert all([len(tokens) == 2, _token_equal(tokens[0], TOKEN_RIGHT_PAREN)])


def test_scan_left_brace():
    tokens = Scanner("{").scan_tokens()
    assert all([len(tokens) == 2, _token_equal(tokens[0], TOKEN_LEFT_BRACE)])


def test_scan_right_brace():
    tokens = Scanner("}").scan_tokens()
    assert all([len(tokens) == 2, _token_equal(tokens[0], TOKEN_RIGHT_BRACE)])


def test_scan_comma():
    tokens = Scanner(",").scan_tokens()
    assert all([len(tokens) == 2, _token_equal(tokens[0], TOKEN_COMMA)])


def test_scan_dot():
    tokens = Scanner(".").scan_tokens()
    assert all([len(tokens) == 2, _token_equal(tokens[0], TOKEN_DOT)])


def test_scan_minus():
    tokens = Scanner("-").scan_tokens()
    assert all([len(tokens) == 2, _token_equal(tokens[0], TOKEN_MINUS)])


def test_scan_plus():
    tokens = Scanner("+").scan_tokens()
    assert all([len(tokens) == 2, _token_equal(tokens[0], TOKEN_PLUS)])


def test_scan_semicolon():
    tokens = Scanner(";").scan_tokens()
    assert all([len(tokens) == 2, _token_equal(tokens[0], TOKEN_SEMICOLON)])


def test_scan_slash():
    tokens = Scanner("/").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_SLASH)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_star():
    tokens = Scanner("*").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_STAR)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_bang():
    tokens = Scanner("!").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_BANG)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_bang_equal():
    tokens = Scanner("!=").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_BANG_EQUAL)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_equal():
    tokens = Scanner("=").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_EQUAL)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_equal_equal():
    tokens = Scanner("==").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_EQUAL_EQUAL)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_greater():
    tokens = Scanner(">").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_GREATER)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_greater_equal():
    tokens = Scanner(">=").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_GREATER_EQUAL)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_less():
    tokens = Scanner("<").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_LESS)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_less_equal():
    tokens = Scanner("<=").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_LESS_EQUAL)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_and():
    tokens = Scanner("and").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_AND)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_class():
    tokens = Scanner("class").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_CLASS)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_else():
    tokens = Scanner("else").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_ELSE)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_false():
    tokens = Scanner("false").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_FALSE)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_fun():
    tokens = Scanner("fun").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_FUN)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_for():
    tokens = Scanner("for").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_FOR)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_if():
    tokens = Scanner("if").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_IF)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_nil():
    tokens = Scanner("nil").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_NIL)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_or():
    tokens = Scanner("or").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_OR)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_print():
    tokens = Scanner("print").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_PRINT)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_return():
    tokens = Scanner("return").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_RETURN)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_super():
    tokens = Scanner("super").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_SUPER)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_this():
    tokens = Scanner("this").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_THIS)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_true():
    tokens = Scanner("true").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_TRUE)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_var():
    tokens = Scanner("var").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_VAR)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_while():
    tokens = Scanner("while").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], TOKEN_WHILE)
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_string():
    tokens = Scanner('"abcdef"').scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], Token(TokenType.STRING, '"abcdef"', "abcdef", 0))
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_number_with_semicolon():
    tokens = Scanner("1.25;").scan_tokens()
    assert len(tokens) == 3
    assert _token_equal(tokens[0], Token(TokenType.NUMBER, "1.25", 1.25, 0))
    assert _token_equal(tokens[1], TOKEN_SEMICOLON)
    assert _token_equal(tokens[2], TOKEN_EOF)


def test_scan_number_without_semicolon():
    tokens = Scanner("90.9").scan_tokens()
    assert len(tokens) == 2
    assert _token_equal(tokens[0], Token(TokenType.NUMBER, "90.9", 90.9, 0))
    assert _token_equal(tokens[1], TOKEN_EOF)


def test_scan_declare_number():
    tokens = Scanner("var v=1.25;").scan_tokens()
    assert len(tokens) == 6
    assert _token_equal(tokens[0], Token(TokenType.VAR, "var", None, 0))
    assert _token_equal(tokens[1], Token(TokenType.IDENTIFIER, "v", None, 0))
    assert _token_equal(tokens[2], TOKEN_EQUAL)
    assert _token_equal(tokens[3], Token(TokenType.NUMBER, "1.25", 1.25, 0))
    assert _token_equal(tokens[4], TOKEN_SEMICOLON)
    assert _token_equal(tokens[5], TOKEN_EOF)


def test_scan_declare_number_with_blank():
    tokens = Scanner("  var v  =   1234.567 ; ").scan_tokens()
    assert len(tokens) == 6
    assert _token_equal(tokens[0], Token(TokenType.VAR, "var", None, 0))
    assert _token_equal(tokens[1], Token(TokenType.IDENTIFIER, "v", None, 0))
    assert _token_equal(tokens[2], TOKEN_EQUAL)
    assert _token_equal(tokens[3], Token(TokenType.NUMBER, "1234.567", 1234.567, 0))
    assert _token_equal(tokens[4], TOKEN_SEMICOLON)
    assert _token_equal(tokens[5], TOKEN_EOF)


def test_scan_declare_string_with_blank():
    tokens = Scanner('  var language  =  "veda" ; ').scan_tokens()
    assert len(tokens) == 6
    assert _token_equal(tokens[0], Token(TokenType.VAR, "var", None, 0))
    assert _token_equal(tokens[1], Token(TokenType.IDENTIFIER, "language", None, 0))
    assert _token_equal(tokens[2], TOKEN_EQUAL)
    assert _token_equal(tokens[3], Token(TokenType.STRING, '"veda"', "veda", 0))
    assert _token_equal(tokens[4], TOKEN_SEMICOLON)
    assert _token_equal(tokens[5], TOKEN_EOF)


def test_scan_if_else_stmt():
    tokens = Scanner(
        """
        if v == true {
            print "abc";
        } else {
            return nil;
        }
    """
    ).scan_tokens()
    assert len(tokens) == 16
    assert _token_equal(tokens[0], TOKEN_IF)
    assert _token_equal(tokens[1], Token(TokenType.IDENTIFIER, "v", None, 1))
    assert _token_equal(tokens[2], TOKEN_EQUAL_EQUAL)
    assert _token_equal(tokens[3], TOKEN_TRUE)
    assert _token_equal(tokens[4], TOKEN_LEFT_BRACE)
    assert _token_equal(tokens[5], TOKEN_PRINT)
    assert _token_equal(tokens[6], Token(TokenType.STRING, '"abc"', "abc", 2))
    assert _token_equal(tokens[7], TOKEN_SEMICOLON)
    assert _token_equal(tokens[8], TOKEN_RIGHT_BRACE)
    assert _token_equal(tokens[9], TOKEN_ELSE)
    assert _token_equal(tokens[10], TOKEN_LEFT_BRACE)
    assert _token_equal(tokens[11], TOKEN_RETURN)
    assert _token_equal(tokens[12], TOKEN_NIL)
    assert _token_equal(tokens[13], TOKEN_SEMICOLON)
    assert _token_equal(tokens[14], TOKEN_RIGHT_BRACE)
    assert _token_equal(tokens[15], TOKEN_EOF)
