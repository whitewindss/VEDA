# from src.veda import Scanner
from src.veda import Scanner, Token, TokenType

# var v=1;
tokens = Scanner(' var language  =  "veda" ; ').scan_tokens()
print("\n".join([str(t) for t in tokens]))