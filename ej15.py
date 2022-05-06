A = int(input("Introduce el valor A: "))
B = int(input("Introduce el valor B: "))

while B>A:
    print("El valor B no puede ser mayor a A.")
    A = int(input("Introduce el valor A: "))
    B = int(input("Introduce el valor B: "))

def mcd(dd, d):
    q = dd/d
    r = dd%d
    if r!=0:
        return mcd(d, r)
    else: return d

maximo = mcd(A, B)

print("El m.c.d de "+ str(A) + " y " + str(B) + " es: " + str(maximo))
