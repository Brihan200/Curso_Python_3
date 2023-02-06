# Ejercicio

print("=================================================")
print("Sistema para determinar cual numero es mas grande")
print("=================================================" + "\n")

num_1 = int(input("Por favor ingrese un numero: "))
num_2 = int(input("Por favor ingrese otro numero: "))
num_3 = int(input("Por favor ingrese otro numero: "))
print("\n")

if num_1 > num_2 and num_1 > num_3:
    print("El numero ", num_1, "es el mas grande de los tres numeros ")
elif num_2 > num_1 and num_2 > num_3:
    print("El numero ", num_2, "es el mas grande de los tres numeros ")
elif num_3 > num_1 and num_3 > num_2:
    print("El numero ", num_3, "es el mas grande de los tres numeros ")
print("Fin.")


# Otra forma de hacerlo
"""
if num_1 > num_2 and num_1 > num_3:
    print("El numero ", num_1, "es el mas grande de los tres numeros ")
else:
    if num_2 > num_1 and num_2 > num_3:
        print("El numero ", num_2, "es el mas grande de los tres numeros ")
    else:
        print("El numero ", num_3, "es el mas grande de los tres numeros ")
"""
