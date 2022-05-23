# recibir un parámetro n ingresado por el usuario, y mostrar los primeros n pares.

def obtenerNumero():
    return int(input("Ingrese un número: "));

# Ahora, donde no se considere el cero:
#se recorre la primera función desde 0 
#aqui estará mostrando de 2 en 2 

def mostrarPares(numero):
    for i in range(numero*2, ++2): 
        print(i);                   

# sumar todos los valores impares desde 0 hasta n, donde n es ingresado por el usuario.

def mostrarParesSinCero(numero):
    for i in range(2, (numero*2)+2, ++2):
        print(i);

# el usuario ingresa dos valores, el límite inferior (min) y superior(max) para suma de los impares.

def mostrarSumaImpares(numero):
    resultado = 0;
    for i in range(numero):
        if(i%2 != 0):
            resultado += i;
    print(resultado);

# Función que suma los valores impares desde 0 hasta n, donde n es el valor ingresado por usuario.
# primero se definen los valores de los parametros luego se llama a la funcion con un ciclo for que funcionara
# hasta que el numero sea menor o igual a n dentro del rango dado por el usuario
#si el numero es impar se suma y se imprime

def mostrarSumaImparesLimites(inferior, superior):
    resultado = 0;
    for i in range(inferior, superior):
        if(i%2 != 0):
            resultado += i;
    print(resultado);

# Función que calcula el Fibonacci de n elementos.
#se define parametros para la funcion
#se condiciona con un if el cual si el numero es menor  a 2 que se imprima el elemento
#  y si no se llama a la funcion fibonacci.

def fibonacci(elementos):
    if elementos < 2:
        return elementos;
    else:
        return fibonacci(elementos-1) + fibonacci(elementos-2);

# Función fibonacci n veces.
#se comienza a iterar con un ciclo for para mostrar la sucesión de fibonacci.
#se asigna el valor que ingreso el usuario para recorrerlo en un ciclo for.

def mostrarFibonacci(ocurrencias):
    for i in range(ocurrencias+1):
        print(fibonacci(i));       

