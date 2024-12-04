import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'print': 'PRINT',
    'append': 'APPEND',
    'func': 'FUNC',
    'return': 'RETURN' 
}

tokens = [
    'NUMBER', 'ID', 'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LESS', 'GREATER',
    'AND', 'OR', 'NOT', 'SEMICOLON', 'COMMA', 'STRING','LSQUARE', 'RSQUARE',
    'PERIOD'
] + list(reserved.values())

t_PERIOD = r'\.'
t_LSQUARE    = r'\['
t_RSQUARE    = r'\]'

t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_EQUALS     = r'='
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACE     = r'\{'
t_RBRACE     = r'\}'
t_LESS       = r'<'
t_GREATER    = r'>'
t_AND        = r'&&'
t_OR         = r'\|\|'
t_NOT        = r'!'
t_SEMICOLON  = r';'
t_COMMA      = r','

t_ignore = ' \t'

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1] 
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()