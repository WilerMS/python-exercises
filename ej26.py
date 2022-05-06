lista_enteros = [int(i) for i in input("Introduce tu lista de números separados por comas: ").split(",")]

i = len(lista_enteros)-1
while i>=0:
    print(lista_enteros[i], end=",")
    i -= 1