str_fecha = input("Introduce una fecha en el siguiente formato: DD/MM/AAAA \n")

def format_fecha(fecha):
    array_fecha = []
    for n in fecha.split("/"):
        array_fecha.append(int(n))
    return array_fecha

def comprobar_bisiesto(anyo):
    if anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0):
        return True
    else: return False

def validar_fecha(fecha):
    if fecha[0]<1 or fecha[1]<1 or fecha[2]<0 or fecha[1]>12: 
        return False
    elif fecha[1] in [4, 6, 9, 11] and fecha[0] > 30:
        return False
    elif fecha[1] in [1, 3, 5, 7, 8, 10, 12] and fecha[0] > 31:
        return False
    elif fecha[1] == 2:
        if comprobar_bisiesto(fecha[2]) and fecha[0] > 29:
            return False
        elif fecha[0] > 28: return False 
    return True

while not validar_fecha(format_fecha(str_fecha)):
    print("La fecha introducida no es válida")
    fecha = input("Introduce una fecha en el siguiente formato: DD/MM/AAAA \n")


def calc_siguiente(fecha):
    if fecha[1] in  [4, 6, 9, 11] and fecha[0] < 30:
            return [fecha[0]+1, fecha[1], fecha[2]]
    elif fecha[1] in  [1, 3, 5, 7, 8, 10] and fecha[0] < 31:
            return [fecha[0]+1, fecha[1], fecha[2]]
    elif fecha[1] == 12:
        if fecha[0] < 31:
            return [fecha[0]+1, fecha[1], fecha[2]]
        else: return [1, 1, fecha[2]+1]
    elif fecha[1] == 2:
        if comprobar_bisiesto(fecha[2]) and fecha[0] < 29:
            return [fecha[0]+1, fecha[1], fecha[2]]
        elif fecha[0] < 28:
            return [fecha[0]+1, fecha[1], fecha[2]]
    return [1, fecha[1]+1, fecha[2]]

fecha = calc_siguiente(format_fecha(str_fecha))

print("El dia siguiente a " + str_fecha + " es: " + str(fecha[0]) + "/" + str(fecha[1]) + "/" + str(fecha[2]))