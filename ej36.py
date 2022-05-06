from random import randint

def generar_array(cantidad):
    datos = []
    for i in range(cantidad):
        datos.append(str(randint(1, 99)))
    return datos

def selection_sort(array):
    array = array.copy()
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if int(array[i])>int(array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

def quick_sort(array):
    if len(array)<=1: 
        return
    if len(array)==2:
        if array[0]>array[1]:
            temp = array[0]
            array[0] = array[1]
            array[1] = temp
        return

    pivot = array[0]
    izquierda, derecha = [], []

    for i in array:
        if int(i)<int(pivot):
            izquierda.append(i)
        elif int(i)>int(pivot):
            derecha.append(i)

    quick_sort(izquierda)
    quick_sort(derecha)

    for i in range(len(array)):
        if i<len(izquierda):
            array[i] = izquierda[i]
        elif  i == len(izquierda):
            array[i]=pivot
        else:
            array[i] = derecha[i]





def merge_sort():
    return


cantidad = int(input("Introduce el tamaño del array a generar: "))
array_desordenado = generar_array(cantidad)
array_ordenado = selection_sort(array_desordenado)

print(" ".join(array_desordenado))
print(" ".join(array_ordenado))