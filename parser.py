import ply.yacc as yacc
from lexer_rules import tokens

# Diccionario para almacenar las funciones definidas
functions = {}

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

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Definición de programa para múltiples funciones y sentencias
def p_program(p):
    '''program : function program
               | statement program
               | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + (p[2] if p[2] is not None else [])
    else:
        p[0] = []

# Definición de funciones
def p_function_definition(p):
    'function : FUNCION ID LPAREN parameters RPAREN block'
    function_name = p[2]
    parameters = p[4]
    body = p[6]
    functions[function_name] = {'parameters': parameters, 'body': body}
    print(f"Función '{function_name}' definida con parámetros {parameters} y cuerpo {body}")

# Parámetros de función
def p_parameters(p):
    '''parameters : parameters COMA ID
                  | ID
                  | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] is not None else []
    else:
        p[0] = p[1] + [p[3]]

# Llamada a función
def p_function_call(p):
    'expression : ID LPAREN arguments RPAREN'
    function_name = p[1]
    arguments = p[3]
    if function_name in functions:
        func = functions[function_name]
        if len(arguments) == len(func['parameters']):
            local_context = dict(zip(func['parameters'], arguments))
            print(f"Llamando a la función: {function_name} con argumentos {arguments}")
            p[0] = execute_block(func['body'], local_context)
        else:
            print(f"Error: Número de argumentos incorrecto en la llamada a {function_name}")
            p[0] = None
    else:
        print(f"Error: Función {function_name} no definida")
        p[0] = None

# Retorno de función
def p_return_statement(p):
    'statement : RETURN expression PTCOMA'
    p[0] = ('return', p[2])

# Bloque de código
def p_block(p):
    '''block : LLAVIZQ statement_list LLAVDER'''
    p[0] = p[2]

def p_statement_list(p):
    '''statement_list : statement
                      | statement statement_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

# Definición de statement para imprimir
def p_imprimir_statement(p):
    '''statement : IMPRIMIR LPAREN expression RPAREN
                 | IMPRIMIR LPAREN expression RPAREN PTCOMA'''
    print(p[3])  # Imprime el resultado de la expresión

# Argumentos en llamadas a funciones
def p_arguments(p):
    '''arguments : expression
                 | expression COMA arguments'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# Producción vacía
def p_empty(p):
    'empty :'
    p[0] = None

# Manejador de errores
def p_error(p):
    print("Error de sintaxis en la entrada")

# Ejecutar el bloque de la función
def execute_block(block, context):
    result = None
    for statement in block:
        if isinstance(statement, tuple) and statement[0] == 'return':
            result = statement[1]
            break
    return result

# Construir el parser
parser = yacc.yacc(start='program')
