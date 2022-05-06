num = input("Introduce un número de 4 cifras: ")

while len(num)!=4:
    print("El número introducido no es de cuatro cifras.")
    num = input("Introduce un número de 4 cifras: ")


def Menor(num):
    num = [int(i) for i in num]
    num = sorted(num)
    num = [str(i) for i in num]
    return "".join(num)

def Mayor(num):
    num = [int(i) for i in num]
    num = sorted(num, reverse=True)
    num = [str(i) for i in num]
    return "".join(num)

print(Menor(num))
print(Mayor(num))