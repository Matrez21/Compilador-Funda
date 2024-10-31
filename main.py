from lexer_rules import lexer
from parser import parser

# Entrada para analizar
data = "(3 + 4) * 5"

# Ejecutar el lexer
lexer.input(data)
print("Tokens:")
for tok in lexer:
    print(tok)

# Ejecutar el parser
result = parser.parse(data)
print("\nResultado:", result)
