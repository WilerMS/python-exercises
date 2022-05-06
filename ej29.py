M = int(input("Introduce el numero de filas de la matriz: "))
N = int(input("Introduce el numero de columnas de la matriz: "))

def matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(int(input("Introduce el valor (" + str(i) + ", " + str(j) + "): ")))
    return matriz

def imprimir_matriz(matriz):
    resultado = ""
    for i in matriz:
        for j in i:
            resultado += str(j)
            resultado += " "
        resultado += "\n"
    return resultado

def traspuesta(matriz):
    traspuesta = [] 
    lista_columnas = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j not in lista_columnas:
                traspuesta.append([])
                lista_columnas.append(j)
            traspuesta[j].append(matriz[i][j])
    return traspuesta

matriz = matriz(M, N)
traspuesta = traspuesta(matriz)

print("\nMatriz dada: \n")
print(imprimir_matriz(matriz) + "\n")
print("Matriz traspuesta: \n")
print(imprimir_matriz(traspuesta))