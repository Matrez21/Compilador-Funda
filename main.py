from lexer_rules import lexer
from parser import parser

def procesar_entrada(data):
    # Ejecutar el lexer y el parser para la entrada proporcionada
    lexer.input(data)
    print("Tokens:")
    for tok in lexer:
        print(tok)
    result = parser.parse(data)
    return result

def main():
    print("Bienvenido al intérprete.")
    print("Escribe expresiones para evaluarlas o 'salir' para terminar.")
    print("--------------------------------------------------------------")
    print("Instrucciones:")
    print("1. Usa 'imprimir' para mostrar el resultado de una expresión.")
    print("   Ejemplo: imprimir(5 + 3 * 2);")
    print("2. Puedes realizar operaciones aritméticas: +, -, *, /")
    print("   Ejemplo: imprimir(10 - 2 / 2);")
    print("3. Escribe 'salir' para finalizar el intérprete.")
    print("--------------------------------------------------------------")
    
    while True:
        try:
            entrada = input(">>> ")
            if entrada.lower() == "salir":
                print("Finalizando el intérprete. ¡Hasta luego!")
                break
            resultado = procesar_entrada(entrada)
            if resultado not in [None, []]:
                print("\nResultado:", resultado[0] if isinstance(resultado, list) else resultado)
            else:
                print("\nResultado: Ningún valor retornado.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
