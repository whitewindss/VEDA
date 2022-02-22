# from src.veda import Scanner
from src.veda.scan import Scanner

# var v=1;
tokens = Scanner("var").scan_tokens()
print("\n".join([str(t) for t in tokens]))