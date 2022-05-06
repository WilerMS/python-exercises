num = int(input("Introduce un numero: "))

def primo(num):
    i=2
    while i<num:
        if num % i == 0:
            return False
        i += 1
    return True

if primo(num):
    print("El numero " + str(num) + " es primo")
else: print("El numero " + str(num) + " no es primo")