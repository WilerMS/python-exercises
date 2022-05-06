num = int(input("Introduce un número: "))

for i in range(num+1):
    for j in range(i):
        print(i, end="")
    print("\n")

