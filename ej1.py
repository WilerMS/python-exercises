num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if num1<num2 and num1<num3:
    if num2<num3:
        print(str(num1)+","+str(num2)+","+str(num3))
    else: print(str(num1)+","+str(num3)+","+str(num2))
elif num2<num1 and num2<num3:
    if num1<num3:
        print(str(num2)+","+str(num1)+","+str(num3))
    else: print(str(num2)+","+str(num3)+","+str(num1))
elif num3<num1 and num3<num2:
    if num2<num1:
        print(str(num3)+","+str(num2)+","+str(num1))
    else: print(str(num3)+","+str(num1)+","+str(num2))