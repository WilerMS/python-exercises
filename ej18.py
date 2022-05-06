import math
num = int(input("Introduce el número de latas a apilar: "))

while num<=0:
    print("Tiene que haber más de una lata.")
    num = int(input("Introduce un número válido de latas a apilar: "))

def validar_latas(num):
    n = (-1 + math.sqrt(1 + 4*2*num)) / 2
    if n % 1 == 0:
        return True
    return False


if validar_latas(num):
    print("Correcto, se pueden apilar " + str(num) + " latas triangularmente.")
else: 
    print("No, no se pueden apilar " + str(num) + " latas triangularmente.")
