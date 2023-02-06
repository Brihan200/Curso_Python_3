# Concatenacion f con strings

"""
f-strings -> Se pueden agregar variedad de expresiones validas ej. f"{4+1}" -> 5
"""
#asi:
nombre = "Carlos"
edad = 22
print(f"Hola {nombre} su edad es {edad}" + "\n")

# Otro ejemplo
print("Otro ejemplo: ")
print(f"El resultado de la suma es -> {4+1}" + "\n")

# Otro ejemplo
print("Otro ejemplo: ")
nombre_2 = "Brihan"
estatura = 1.80
edad_2 = 25

print(f"Hola {nombre_2} tienes {edad_2} años y mides {estatura} centimetros." + "\n")

# Otro ejemplo
print("Otro ejemplo: ")
nombre_3 = input("Cual es tu nombre?: ")
num_uno = int(input("Introduce un numero: "))
num_dos = int(input("Introduce otro numero: "))

print(f"Tu nombre es {nombre_3}, el resultado de {num_uno} + {num_dos} es: {num_uno+num_dos}")


