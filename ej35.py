#Se ingresan dos números para calcular su suma de forma manual.

from random import randint

def obt_array(num):
    array = [i for i in num]
    return array

def igualar_longitud(num1, num2):
    longitud, ceros = len(num1) - len(num2), ""
    for i in range(abs(longitud)):
        ceros += " "
    if longitud < 0:
        num1 = ceros + num1
    elif longitud > 0:
        num2 = ceros + num2
    return (num1, num2)

def calcular(num1, num2):
    j = len(num1)
    resultado = [" " for i in range(j)]
    acarreo = ["0" for i in range(j)]
    
    while j > 0:
        input("\nPulse ENTER para continuar con la suma")
        
        print(" ", end="")
        for i in acarreo:
            if i == "0": print("  ", end="")
            else: print(" " + i, end="")
            
        print("\n  "+ " ".join(num1))
        print("+ " + " ".join(num2))
        print(u'\u2500\u2500' * (len(resultado)+1))

        if num1[j-1] == " ":
            suma = str(int(num2[j-1]) + int(acarreo[j-1]))
        elif num2[j-1] == " ":
            suma = str(int(num1[j-1]) + int(acarreo[j-1]))
        else:
            suma = str(int(num1[j-1]) + int(num2[j-1]) + int(acarreo[j-1]))
        
        if len(suma)>1:
            resultado[j-1] = suma[1]
            acarreo[j-2] = suma[0]
            if j == 1: resultado.insert(0, suma[0])
        else:
            resultado[j-1] = suma
            acarreo[j-2] = "0"

        if len(resultado)==len(num1): print("  ", end="")
        print(" ".join(resultado))

        j -= 1


#Obteniendo los dos números escritos por el usuario
num1 = input("Introduce el primer valor a sumar: ")
num2 = input("Introduce el segundo valor a sumar: ")
#Igualamos las longitudes de los dos números
(num1, num2) = igualar_longitud(num1, num2)
#Pasamos los numeros de string a Arrays
num1, num2 = obt_array(num1), obt_array(num2)
calcular(num1, num2)





