A = int(input("Introduce el primer numero: "))
B = int(input("Introduce el segundo numero: "))

while B == 0:
    print("La división entre 0 no es posible")
    B = int(input("Introduce el segundo numero: "))

def cociente(num1, num2):
    cociente = 0
    while num1>=num2:
        num1 -= num2
        cociente += 1
    resto = num1
    return [cociente, resto]

resultado = cociente(A, B)
cociente = resultado[0]
resto = resultado[1]
print("El cociente de " + str(A) + " / " + str(B) + " es: " + str(cociente))
print("El resto de " + str(A) + " / " + str(B) + " es: " + str(resto))