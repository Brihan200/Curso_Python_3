# Operadores relacionales

"""
< -> Menor que
> -> Mayor que
== -> Comparacion o Igual a
!= -> No igual a (diferente)
<= -> Menor que o igual a
>= -> Mayor que o igual a
"""

# Ejemplo

print("Introduce dos numeros a comparar: " + "\n")
num_uno = int(input("Introduce el primer numero: "))
num_dos = int(input("Introduce el segundo numero: "))

print("\n Los numeros a comparar son: ", num_uno, "y" ,num_dos, "\n")

if num_uno == num_dos:
    print("El numero es igual ...")
if num_uno != num_dos:
    print("El numero es diferente...")
if num_uno < num_dos:
    print("El numero es menor...")
if num_uno > num_dos:
    print("El numero es mayor...")
if num_uno <= num_dos:
    print("El numero es menor o igual...")
if num_uno >= num_dos:
    print("El numero es mayor o igual...")
print("Fin.")

