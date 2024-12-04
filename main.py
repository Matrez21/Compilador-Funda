from parser import ejecutar_codigo

codigo = '''



print("------------------------------------");
print("-------  Manejo de FUNCIONES  -------");
print("------------------------------------");



func suma(x, y) {
    return x + y;
}

print(suma(5, 3));

func multiplicar(a, b) {
    return a * b;
}

print(multiplicar(4, 6));

print(suma(multiplicar(40,2) , multiplicar(20,20)));



print("------------------------------------");
print("-------  Manejo de ARREGLOS  -------");
print("------------------------------------");



arr = [1, 2, 3, 4];
print(arr);

lista = {};
lista.append(1);
lista.append(2);
print(lista);



print("------------------------------------");
print("-  Manejo de DECLARACION DE VARIABLES  -");
print("------------------------------------");



x = 10;
y = 0;

mensaje = "hola mundo";

print(mensaje);



print("------------------------------------");
print("-----  Manejo de CONDICIONALES  -----");
print("------------------------------------");



if (x > 5) {
    print("La condicion del IF se cumplio. x es mayor que 5");
} else {
    print("La condicion del ELSE se cumplio. x no es mayor que 5");
}



print("------------------------------------");
print("---  Manejo de CICLOS (while/for)  ---");
print("------------------------------------");



while (x > 0) {
    print("x es:", x);
    x = x - 1;
}


print("------------------------------------");

for (z = 0; z < 5; z = z + 1) {
    print("z vale", z);
}

print("------------------------------------");


'''

ejecutar_codigo(codigo)