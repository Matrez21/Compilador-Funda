import ply.lex as lex

# Diccionario de palabras reservadas
reserved = {
    'funcion': 'FUNCION',
    'return': 'RETURN',
    'imprimir': 'IMPRIMIR',
}

# Lista de tokens
tokens = [
    'NUMBER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 
    'LPAREN', 'RPAREN', 'ID', 'COMA', 'PTCOMA', 
    'LLAVIZQ', 'LLAVDER'
] + list(reserved.values())

# Reglas de expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMA = r','
t_PTCOMA = r';'
t_LLAVIZQ = r'\{'
t_LLAVDER = r'\}'

# Regla para identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica si es una palabra reservada
    return t

# Regla para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejador de errores
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Inicializar el lexer
lexer = lex.lex()
