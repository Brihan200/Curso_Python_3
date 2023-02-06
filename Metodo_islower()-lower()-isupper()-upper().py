# Metodos islower(), lower(), isupper(), upper()

"""
* islower() -> nombre_variable.islower() // Retorna un valor booleano(True o False) verificando si toda la cadena estan en minisculas

* lower() -> nombre_variable.lower() // Convierte todo a minisculas

* isupper() -> nombre_variable.isupper() // Retorna un valor booleano(True o False) verificando si toda la cadena estan en mayusculas

* upper() -> nombre_variable.upper() // Convierte todo a mayusculas
"""

# Ej
variable = "La Geekipedia"
print(variable.islower())
variable = variable.lower()
print(variable)
print(variable.isupper())
print(variable.upper())
print(variable)

print()

# Otro ejemplo
string = input("Por favor introduce un String: ")
print(f"\n¿Todas las letras estan en minusculas?: {string.islower()}")
string = string.lower()
print(f"String en minusculas: {string}")


print(f"\n¿Todas las letras estan en mayusculas?: {string.isupper()}")
print(f"String en mayusculas: {string.upper()}")
print(f"String original: {string}")

