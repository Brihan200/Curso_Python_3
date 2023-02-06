# Ejercicio Practico 2

print("====================")
print("Sistema para calcular si un numero es par o impar: ")
print("=====================" + "\n")


nombre_usuario = input("Por favor ingrese su nombre: ")
nombre_usuario = nombre_usuario.upper()
numero = int(input("Por favor ingrese un numero entero: "))
print("\n")

if numero % 2 == 0:
    print("Usuario", nombre_usuario, " el numero ", numero, " es par")
elif numero % 2 == 1 :
    print("Usuario", nombre_usuario, " el numero", numero, "es impar")
print("Fin.")
