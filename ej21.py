num = input("Introduce el número: ")
caracteres = [i for i in num]

num = ""
for n in reversed(caracteres):
    num += n

print(num)
