lista_enteros = [int(i) for i in input("Introduce tu lista de números separados por comas: ").split(",")]

def sumas(lista):
    sumas_pares = 0
    sumas_impares = 0

    i = 0 
    while len(lista)>i:
        if i % 2 == 0:
            sumas_pares += lista[i]
        else: sumas_impares += lista[i]
        i += 1
    return {"suma_pares": sumas_pares, "sumas_impares": sumas_impares}

print(sumas(lista_enteros))