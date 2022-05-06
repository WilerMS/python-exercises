from random import randint

num = int(input("Introduce el número de cifras: "))
while num>=10:
    print("El número maximo de digitos debe ser 10.")
    num = int(input("Introduce el número de cifras: "))

def comprobar_digitos(numero, digito):
    for i in numero:
        if i == str(digito):
            return True
    return False

def generar_aleatorio(num_cifras):
    num = ""
    while len(num)<num_cifras:
        temp = randint(0, 9)
        if not comprobar_digitos(num, temp):
            num += str(temp)
    return num

def comprobar_adivinado(numero):
    numero = [int(i) for i in numero]
    for i in range(len(numero)-1):
        for j in range(i+1, len(numero)):
            if numero[i] == numero[j]:
                return True
    return False

def generar_pista(aleatorio, respuesta):
    resultado = ""
    for j in range(len(respuesta)):
        if comprobar_digitos(aleatorio, respuesta[j]):
            for i in range(len(aleatorio)):
                if aleatorio[i] == respuesta[j]:
                    if i == j:
                        resultado += respuesta[j] + "+ "
                    else: resultado += respuesta[j] + "- "
        else: resultado += respuesta[j] + " "
    return resultado

def comprobar(aleatorio, respuesta):
    if (aleatorio == respuesta): return True
    return False

aleatorio = generar_aleatorio(num)
print("\nSe ha generado el número aleatorio de "+ str(num) +" cifras")
print("\nEmpecemos!")

Terminada = False
Win = False
Lose = False
num_intentos = 0
while num_intentos<=5:
    while not Terminada:
        resp = input("\nIntroduce un número para adivinar el número secreto: ")
        while len(resp)!=num:
            print("\nEl número debe ser de la misma longitud.")
            resp = input("\nIntroduce un número de la misma longitud: ")
        while comprobar_adivinado(resp):
            print("\nNo se debe repetir ninguno de los dígitos introducidos.")
            resp = input("\nIntroduce el número otra vez: ")

        input("\nVamos a comprobar si " + resp + " es el número buscado.")
        print("\n...")
        print("...")
        print("...")

        if (comprobar(aleatorio, resp)):
            Terminada = True
            Win = True
            num_intentos = 11
        else:
            if num_intentos==0:
                print("No! Este no es el número que andamos buscando. \nTe daremos una pista :D")
                print("\nPor cada dígito acertado se añadirá un signo a su derecha.")
                print("Si has acertado un dígito y su posición será un +, sino coincide la posición será un menos.")
                print("Por último, si no se encuentra en el número aleatorio, solo saldrá el dígito.")
                input("\nPresiona ENTER para generar la pista, Suerte! :D\n")
            else:
                print("\nNo! Este tampoco es el número que buscamos.")    
                input("\nTe daremos otra pista, Suerte! :D\n")
            print(generar_pista(aleatorio, resp))
            num_intentos += 1
            if num_intentos>5: 
                Terminada = True
                Lose = True

if Lose == True:
    print("\nHas perdido, el número generado era: " + aleatorio)

elif Win == True:
    print("\nHas acertado, El número aleatorio es:  " + aleatorio)

    
