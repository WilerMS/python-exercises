lista_enteros = [int(i) for i in input("Introduce tu lista de números separados por comas: ").split(",")]

def mayor_menor(lista):
    mayor = lista[0]
    menor = lista[0]
    repeat_mayor = 1
    repeat_menor = 1
    i = 1
    while len(lista)>i:
        if lista[i]>mayor:
            mayor = lista[i]
            repeat_mayor = 1
        elif lista[i]==mayor:
            repeat_mayor += 1
        
        if lista[i]<menor:
            menor = lista[i]
            repeat_menor = 1
        elif lista[i]==menor:
            repeat_menor +=1
        i += 1
    return {"mayor": mayor, "menor": menor, "repeat_mayor":repeat_mayor, "repeat_menor":repeat_menor, "lista": lista}

print(mayor_menor(lista_enteros))
        