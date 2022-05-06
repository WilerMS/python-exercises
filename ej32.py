orden = int(input("Orden de la matriz a calcular: "))

def rotar(vector):
    nuevo_vector = [i for i in vector]
    for i in range(len(vector)):
        if i == 0:
            nuevo_vector[0] = vector[len(vector)-1]
        else:
            nuevo_vector[i] = vector[i-1]
    return nuevo_vector

def imprimir_matriz(matriz):
    resultado = ""
    for i in matriz:
        for j in i:
            resultado += str(j)
            resultado += " "
        resultado += "\n"
    return resultado

def matriz(orden):
    matriz = []
    for i in range(orden):
        matriz.append([])
        for j in range(orden):
            matriz[i].append(None)
    return matriz

def cuadrado_latino(matriz):
    valores = [i for i in range(len(matriz[0]))]
    for i in range(len(matriz)):
        if i == 0: matriz[i] = valores
        else: matriz[i]  = rotar(matriz[i-1])
    return matriz

matriz = matriz(orden)
cuadrado = cuadrado_latino(matriz)

print("\nEl cuadrado latino de orden " + str(orden) + " es: \n")
print(imprimir_matriz(cuadrado))
