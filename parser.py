import ply.yacc as yacc
from lexer_rules import tokens

# Diccionario de variables
variables = {}

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

# Expresiones aritméticas
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_float(p):
    'expression : FLOAT'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_variable(p):
    'expression : ID'
    p[0] = variables.get(p[1], f"Variable '{p[1]}' no definida")

def p_statement_assign(p):
    'statement : ID EQUALS expression PTCOMA'
    variables[p[1]] = p[3]
    print(f"Variable '{p[1]}' asignada con valor {p[3]}")

# Definición de la instrucción imprimir
def p_statement_imprimir(p):
    '''statement : IMPRIMIR LPAREN expression RPAREN PTCOMA'''
    print(f"Imprimir: {p[3]}")

# Definición de programa para múltiples funciones y sentencias
def p_program(p):
    '''program : statement program
               | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + (p[2] if p[2] is not None else [])
    else:
        p[0] = []

# Producción vacía
def p_empty(p):
    'empty :'
    p[0] = None

# Manejador de errores
def p_error(p):
    print("Error de sintaxis en la entrada")

# Construir el parser
parser = yacc.yacc(start='program')
