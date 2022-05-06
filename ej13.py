num = int(input("Introduce un numero: "))

def primo(num):
    i=2
    while i<num:
        if num % i == 0:
            return False
        i += 1
    return True

def generar_primos(num):
    array_primos = []
    i = 2
    while len(array_primos)<num:
        if primo(i):
            array_primos.append(i)
        i+=1
    return array_primos

primeros_primos = generar_primos(num)

print("Los primeros " + str(num) + " números primos son: ", end=" ")
print(primeros_primos)