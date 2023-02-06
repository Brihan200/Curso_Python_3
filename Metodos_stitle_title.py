# Metodos istitle() y title()

"""
Sintaxis -> nombre_variable.istitle() -> Devuelve un valor booleano (True o False)
            nombre_variable.title() -> Obtiene el valor de la cadenay aplica el formato indicado
"""

# Ejemplo istitle()
print("* istitle: ")
nombre = "bRihan SuArEz"
print(nombre.istitle())
print(nombre, "\n")

# Ejemplo title()
print("* title: ")
nombre_2 = "bRihan SuArEz"
print(nombre_2.title())
print(nombre_2, "\n")

# Otro ejemplo:
print("Otro ejercicio: ")
first_name = input("Por favor ingrese su nombre: ")
last_name = input("Por favor ingrese su apellido: ")
full_name = f"{first_name} {last_name}"

print()
print(f"¿El formato del metodo title() se ha aplicado?: {full_name.istitle()}")
print(f"Aplicando el metodo title(): {full_name.title()}")
print(f"Volvemos a imprimir el nombre: {full_name}")

print()
full_name = full_name.title()
print(f"¿El formato del metodo title() se ha aplicado?: {full_name.istitle()}")
print(f"Se ha aplicado el metodo title() de manera permanente: {full_name}")
