import math
num = int(input("Introduce el número de latas a apilar: "))

while num<=0:
    print("Tiene que haber más de una lata.")
    num = int(input("Introduce un número válido de latas a apilar: "))

def validar_latas_triangulares(num):
    n = (-1 + math.sqrt(1 + 4*2*num)) / 2
    if n % 1 == 0:
        return True
    return False

def validar_latas_cuadradas(num):
    n = math.sqrt(num)
    if n % 1 == 0:
        return True
    return False

if validar_latas_triangulares(num):
    print("Se pueden apilar " + str(num) + " latas triangularmente.")
else: 
    print("No se pueden apilar " + str(num) + " latas triangularmente.")

if validar_latas_cuadradas(num):
    print("Se pueden apilar " + str(num) + " latas en estructuras cuadradas.")
else: 
    print("No se pueden apilar " + str(num) + " latas en estructuras cuadradas.")