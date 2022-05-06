variable = int(input("Introduce el valor de la variable x : "))
grado = int(input("Introduce el grado del polinomio: "))
coeficientes = [int(i) for i in input("Introduce los coeficientes separados por comas: ").split(",")]

while len(coeficientes)!=grado+1:
    print("El número de coeficientes no coincide con el grado del polinomio.")
    coeficientes = [int(i) for i in input("Introduce los coeficientes separados por comas: ").split(",")]


def evaluar_polinomio(variable, grado, coeficientes):
    resultado = 0
    for n in coeficientes:
        resultado += variable**grado*n
        grado -= 1
    return resultado

polinomio = evaluar_polinomio(variable, grado, coeficientes)
print("La evaluación del polinomio es: ", end="")
print(polinomio)