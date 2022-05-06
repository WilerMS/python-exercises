orden = int(input("Introduce el orden de la matriz: "))

def matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(None)
            if i == j:
                matriz[i][j] = 1
            else: matriz[i][j] = 0
    return matriz

def imprimir_matriz(matriz):
    resultado = ""
    for i in matriz:
        for j in i:
            resultado += str(j)
            resultado += " "
        resultado += "\n"
    return resultado

matriz = matriz(orden, orden)

print("\nMatriz unitaria de orden "+ str(orden) + ": \n")
print(imprimir_matriz(matriz))