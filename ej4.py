num = int(input("Introduce un número: "))

def factorial_bucle(num):
    factorial = 1
    while num>1:
        factorial *= num
        num-=1
    return factorial

def factorial_recursivo(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial_recursivo(num - 1)

print("El factorial de " + str(num) + "con factorial_bucle() es: " + str(factorial_bucle(num)))
print("El factorial de " + str(num) + "con factorial_recursivo() es: " + str(factorial_recursivo(num)))