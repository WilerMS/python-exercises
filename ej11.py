num = int(input("Introduce el número a comprobar: "))

while num < 0:
    print("Tienes que ingresar un número entero y positivo")
    num = int(input("Introduce el número a comprobar: "))

def divisores(num): 
    resultado = []
    i = 1
    while i < num:
        if num % i == 0:
            resultado.append(i)
        i += 1
    return resultado

def num_perfecto(divisores):
    resultado = 0
    for n in divisores:
        resultado += n
    return resultado

if num_perfecto(divisores(num)) == num:
    print("El número " + str(num) + " es perfecto")
else:  print("El número " + str(num) + " no es perfecto")