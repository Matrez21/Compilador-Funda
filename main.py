from lexer_rules import lexer
from parser import parser

def procesar_entrada(data):
    # Ejecutar el lexer y el parser para la entrada proporcionada
    lexer.input(data)
    #print("Tokens:")
    #for tok in lexer:
    #   print(tok)
    result = parser.parse(data)
    return result

def procesar_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding="utf-8") as file:
            contenido = file.read()
        resultado = procesar_entrada(contenido)
        if resultado not in [None, []]:
            print("\nResultado:", resultado[0] if isinstance(resultado, list) else resultado)
        else:
            print("\nResultado: Ningún valor retornado.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
    except Exception as e:
        print(f"Error procesando el archivo: {e}")


def main():
    print("Bienvenido al intérprete.")
    print("Escribe expresiones para evaluarlas o 'salir' para terminar.")
    print("--------------------------------------------------------------")
    print("Modo de uso:")
    print("1. Modo interactivo: Escribe 'salir' para finalizar el intérprete.")
    print("2. Para ejecutar un archivo: Escribe 'archivo <ruta_del_archivo>'")
    print("   Ejemplo: archivo test_program.txt")
    print("--------------------------------------------------------------")

    while True:
        try:
            entrada = input(">>> ")
            if entrada.lower() == "salir":
                print("Finalizando el intérprete. ¡Hasta luego!")
                break
            elif entrada.startswith("archivo "):
                ruta_archivo = entrada.split(" ", 1)[1]
                procesar_archivo(ruta_archivo)
            else:
                resultado = procesar_entrada(entrada)
                if resultado not in [None, []]:
                    print("\nResultado:", resultado[0] if isinstance(resultado, list) else resultado)
                else:
                    print("\nResultado: Ningún valor retornado.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
