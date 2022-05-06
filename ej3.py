lista = input("Introduce tu lista de números: ")
array_lista = lista.split(",")

def comprobar_diez(lista):
    for n in lista:
        if n == "10":
            return True
        else: return False

if comprobar_diez(array_lista):
    print("Hay al menos un diez en la lista")
else: print("No hay ningun diez en la lista")