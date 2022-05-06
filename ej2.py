hora = input('Introduce la hora en el siguiente formato, "HH:mm:ss": ')

hora = hora.split(":")

def sumar_seg(hora, minutos, seg):
    hora = int(hora)
    minutos = int(minutos)
    seg = int(seg)

    if seg<59:
        return [hora, minutos, seg+1]
    elif seg==59:
        if minutos<59:
            return [hora, minutos+1, 0]
        elif minutos==59:
            if hora < 23:
                return [hora+1, 0, 0]
            elif hora == 23:
                return [0, 0, 0]

print(sumar_seg(hora[0], hora[1], hora[2]))