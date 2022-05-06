num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

def mul_sucesiva(num1, num2):
    resultado = 0
    for i in range(num2):
        resultado += num1
    return resultado

print(str(num1) + " x " + str(num2) + " = " + str(mul_sucesiva(num1, num2)))