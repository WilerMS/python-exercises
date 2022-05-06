num = input("Introduce el número: ")

def raiz_digital(num):
    resultado = 0
    caracteres = [int(i) for i in num]
    for n in caracteres:
        resultado += n

    if len(str(resultado)) > 1:
        return raiz_digital(str(resultado))
    else: return str(resultado)

print("La raiz digital de " + str(num) + " es: " + raiz_digital(num))