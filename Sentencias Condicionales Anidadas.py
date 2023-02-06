"""
Sentencias Condicionales Anidadas
"""

# Ejemplo
print("============")
print("Conversor")
print("============" + "\n")

print("Menu de opciones: \n")
print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero." + "\n")

opcion = int(input("Por favor escoga su opcion: "))

if opcion == 1:
    print("\n Conversor de numero a palabra. \n")
    opcion_uno = int(input("¿Cual es el numero que deseas convertir a palabra?: "))
    # Condicion anidadada
    if opcion_uno == 1:
        print("El numero es 'Uno'")
    elif opcion_uno == 2:
        print("El numero es 'Dos'")
    elif opcion_uno == 3:
        print("El numero es 'Tres'")
    elif opcion_uno == 4:
        print("El numero es 'Cuatro'")
    elif opcion_uno == 5:
        print("El numero es 'Cinco'")
    else:
        print("Numero no valido.")
elif opcion == 2:
    print("\n Conversor de palabra a numero. \n")
    opcion_dos = input("¿Cual es la palabra que deseas convertir a numero?: ")
    opcion_dos = opcion_dos.lower() # Convierte toda la cadena de caracteres a minusculas
    # Condicion anidada
    if opcion_dos == 'uno':
        print("El numero es '1'")
    elif opcion_dos == 'dos':
        print("El numero es '2'")
    elif opcion_dos == 'tres':
        print("El numero es '3'")
    elif opcion_dos == 'cuatro':
        print("El numero es '4'")
    elif opcion_dos == 'cinco':
        print("El numero es '5'")
    else:
        print("Palabra no valida.")
else:
    print("Opcion no disponible.")
print("Fin.")
