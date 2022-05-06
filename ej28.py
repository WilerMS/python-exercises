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

def mayor_menor(matriz):
    mayor, menor = matriz[0][0], matriz[0][0]
    posicion_mayor, posicion_menor= [[1, 1]], [[1, 1]]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==mayor:
                posicion_mayor.append([i+1, j+1])
            if matriz[i][j]==menor:
                posicion_menor.append([i+1, j+1])
            if matriz[i][j]>mayor: 
                mayor = matriz[i][j]
                posicion_mayor = [[i+1, j+1]]
            if matriz[i][j]<menor:
                menor = matriz[i][j]
                posicion_menor = [[i+1, j+1]]
    return {"mayor": mayor, "menor": menor, "posicion_mayor":posicion_mayor, "posicion_menor":posicion_menor, "matriz": matriz}

matriz = matriz(M, N)
mayor_menor = mayor_menor(matriz)

print("Matriz generada: \n" + imprimir_matriz(matriz))
print("\nNumero mayor: " + str(mayor_menor["mayor"]))
print("Posiciones: " + str(mayor_menor["posicion_mayor"]))
print("\nNumero menor: " + str(mayor_menor["menor"]))
print("Posiciones: " + str(mayor_menor["posicion_menor"]))



