num = input("Introduce un número de 10 cifras: ")

def capicua(num):
    capicua = ""
    lista_caracteres = [i for i in num]
    i = len(lista_caracteres)-1
    while i>=0:
        capicua += lista_caracteres[i]
        i -= 1
    
    if capicua==num:
        return True
    else: return False

print(capicua(num))
