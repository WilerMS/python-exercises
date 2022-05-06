vector = input("Introduce el vector deseado: ")

def rotar(vector):
    nuevo_vector = vector.copy()
    for i in range(len(vector)):
        if i == 0:
            nuevo_vector[0] = vector[len(vector)-1]
        else:
            nuevo_vector[i] = vector[i-1]
    return nuevo_vector

vector = vector.split(",")
print(vector)
print(rotar(vector))