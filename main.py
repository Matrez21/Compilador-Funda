from parser import ejecutar_codigo

codigo = '''

print("------------------------------------");

x = 10;
y = 0;

mensaje = "hola mundo";

print(mensaje);

print("------------------------------------");

if (x > 5) {
    print("La condición del IF se cumplió. x es mayor que 5");
} else {
    print("La condición del ELSE se cumplió. x no es mayor que 5");
}

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