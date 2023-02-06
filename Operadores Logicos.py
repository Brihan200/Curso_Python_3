# Operadores logicos

"""
Conjuncion -> AND
Disyuncion -> OR
Negacion -> NOT
"""

# AND
num_uno = int(input('Ingrese un numero por favor: '))
num_dos = int(input('Ingrese otro numero por favor: '))
print("\n")

print("AND : ")
if num_uno == 5 and num_dos >= 5:
    print('Ambas condiciones se han cumplido ')
else:
    print("Uno o ambas condiciones no se han cumplido ")
print("\n")

# OR
print("OR : ")
if num_uno == 5 or num_dos >=5:
    print("Una de las dos condiciones se han cumplido")
else:
    print("Ninguna de las condiciones se han cumplido")
print("\n")

# NOT
print("NOT : ")
if not num_dos >5:
    print("La condicion se invirtio y se cumple al ser un numero menor o igual a 5")
else:
    print("No se cumple la condicion porque el numero es mayor a 5")


