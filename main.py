from parser import ejecutar_codigo
from error_handler import errores
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo.txt>")
        return

    archivo = sys.argv[1]
    
    try:
        with open(archivo, 'r') as f:
            codigo = f.read()
        print("Código leido del archivo:")
        print(codigo)
        ejecutar_codigo(codigo)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
    except Exception as e:
        print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()


if errores:
    print("\nSe encontraron los siguientes errores:")
    for e in errores:
        print(e)
else:
    print("Ejecución completada sin errores.")