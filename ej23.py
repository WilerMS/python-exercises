A = int(input("Introduce el primer valor: "))
B = int(input("Introduce el segundo valor: "))

def multiplicar(num1, num2):
    m = num2
    n = num1
    resultado = 0
    lista = []

    while m >= 1:
        if m % 2 != 0:
            lista.append(n)
        m = int(m/2)
        n = n*2

    for n in lista:
        resultado += n
    
    return resultado

print(multiplicar(A, B))