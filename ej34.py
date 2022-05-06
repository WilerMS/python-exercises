from random import randint

def generar_set_aleatorio(cantidad):
    datos = []
    for i in range(cantidad):
        datos.append(randint(1, 99))
    return datos

def generar_set_personal(cantidad):
    datos = []
    for i in range(cantidad):
        datos.append(int(input("Introduce un nuevo valor: ")))
    return datos

def maximo(datos):
    maximo = datos[0]
    for i in datos:
        if i > maximo:
            maximo = i
    return str(maximo)

def minimo(datos):
    minimo = datos[0]
    for i in datos:
        if i < minimo:
            minimo = i
    return str(minimo)

def media(datos):
    suma = 0
    for i in datos:
        suma += i
    media = suma / len(datos)
    return str(media)

def moda(datos):
    diccionario = {}
    repeticiones = 0
    moda = []
    for i in datos:
        if str(i) in diccionario:
            diccionario[str(i)] = diccionario[str(i)] + 1
        else: diccionario[str(i)] = 1
    for key in diccionario:
        if diccionario[key] > repeticiones:
            repeticiones = diccionario[key]
            moda = [key]
        elif diccionario[key] == repeticiones:
            moda.append(key)    
    return ", ".join(moda)

def mediana(datos):
    datos = sorted(datos)
    pos = int(len(datos)/2)
    if len(datos) % 2 == 0:
        mediana = (datos[pos] + datos[pos-1])/2
    else: mediana = datos[pos]
    return str(mediana)

def porcentajes(datos):
    diccionario = {}
    resultado = ""
    for i in datos:
        if str(i) in diccionario:
            diccionario[str(i)]['cantidad'] = diccionario[str(i)]['cantidad'] + 1
            diccionario[str(i)]['porcentaje'] = (diccionario[str(i)]['cantidad'] / len(datos)) * 100
        else: 
            diccionario[str(i)] = {'cantidad': 1}
            diccionario[str(i)]['porcentaje'] = (diccionario[str(i)]['cantidad'] / len(datos)) * 100
    for i in diccionario:
        texto = "\n     [" + i + "] - Cantidad: " + str(diccionario[i]['cantidad']) + ", Porcentaje: " + str(diccionario[i]['porcentaje']) + "%\n"
        resultado += texto
    return resultado

def porcentajes2(datos):
    diccionario = {}
    resultado = ""
    for i in datos:
        if i<10:
            if str(i) in diccionario:
                diccionario[str(i)]['cantidad'] = diccionario[str(i)]['cantidad'] + 1
                diccionario[str(i)]['porcentaje'] = (diccionario[str(i)]['cantidad'] / len(datos)) * 100
            else: 
                diccionario[str(i)] = {'cantidad': 1}
                diccionario[str(i)]['porcentaje'] = (diccionario[str(i)]['cantidad'] / len(datos)) * 100
    for i in diccionario:
        texto = "\n     [" + i + "] - Cantidad: " + str(diccionario[i]['cantidad']) + ", Porcentaje: " + str(diccionario[i]['porcentaje']) + "%\n"
        resultado += texto
    return resultado

input("\nEste es un programa para evaluar tu set de datos.")

print("\nElige una de las siguientes opciones: ")
print("\n1.- Evaluar mi propio set de datos. ")
print("\n2.- Evaluar con números aleatorios ")
opcion = input("\nElige una opción: ")

while opcion not in ["1", "2"]:
    print("\nNo has elegido una opción válida.")
    opcion = input("\nElige una opción: ")

if opcion == "1":
    cantidad = int(input("\nIntroduce la cantidad de elementos de tu set de datos: "))
    datos = generar_set_personal(cantidad)

if opcion == "2":
    cantidad = int(input("\nIntroduce la cantidad de elementos a evaluar: "))
    datos = generar_set_aleatorio(cantidad)

print("\nSe ha generado el set de datos con exito.")
input("\nPresione ENTER para continuar...")

Finalizado = False
while not Finalizado:
    print("\nEste es el set de datos generado:\n ")
    print(datos)
    print("\nElige una de las opciones a calcular:")
    print("\n  1.- Calcular el valor más alto. ")
    print("\n  2.- Calcular el valor más bajo. ")
    print("\n  3.- Calcular la media aritmética. ")
    print("\n  4.- Calcular la moda. ")
    print("\n  5.- Calcular la mediana. ")
    print("\n  6.- Calcular repeticiones y porcentajes de cada valor.")
    print("\n  7.- Calcular Todo.")

    opcion = input("\nElige una de las opciones: ")

    while opcion not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\nNo has elegido una opción válida.")
        opcion = input("\nElige una opción: ")

    if opcion == "1":   resultado = "\nEl valor máximo es: " + maximo(datos)
    elif opcion == "2": resultado = "\nEl valor mínimo es: " + minimo(datos)
    elif opcion == "3": resultado = "\nLa media es: " + media(datos)
    elif opcion == "4": resultado = "\nLa moda es: " + moda(datos)
    elif opcion == "5": resultado = "\nLa mediana es: " + mediana(datos)
    elif opcion == "6": resultado = "\nRepeticiones y porcentajes: " + porcentajes2(datos)
    elif opcion == "7":
        resultado = "\nTodos los datos serán calulados: "
        resultado += "\n\n  1.- El valor máximo es: " + maximo(datos)
        resultado += "\n\n  2.- El valor mínimo es: " + minimo(datos)
        resultado += "\n\n  3.- La media es: " + media(datos)
        resultado += "\n\n  4.- La moda es: " + moda(datos)
        resultado += "\n\n  5.- La mediana es: " + mediana(datos)
        resultado += "\n\n  6.- Repeticiones y porcentajes: \n" + porcentajes(datos) 

    print(resultado)

    print("\n¿Quieres hacer otro calulo son el mismo set de datos?")
    input("\nPresiona ENTER si así es, de lo contrario, cierra el programa.")
