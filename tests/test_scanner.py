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

TOKEN_EQUAL = Token(type=TokenType.EQUAL, lexeme="=", literal=None, line=0)


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
