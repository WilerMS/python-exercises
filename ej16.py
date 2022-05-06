A = int(input("Introduce el valor A: "))
B = int(input("Introduce el valor B: "))

while B>A and A<0 and B<0:
    print("El valor B no puede ser mayor a A, ni pueden ser negativos.")
    A = int(input("Introduce el valor A: "))
    B = int(input("Introduce el valor B: "))

def mcd(dd, d):
    q = dd/d
    r = dd%d
    if r!=0:
        return mcd(d, r)
    else: return d

def mcm(N1, N2):
    return int((N1/N2)*mcd(N1, N2))

minimo = mcm(A, B)

print("El m.c.m de "+ str(A) + " y " + str(B) + " es: " + str(minimo))