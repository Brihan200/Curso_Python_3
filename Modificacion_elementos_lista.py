# Modificar los elementos de una lista

"""
                     -5   -4   -3   -2   -1
Sintaxis: vocales = ["a", "e", "i", "o", "u"]
                     0/1  1/2  2/3  3/4  4/5
                     
          vocales[1] = "x" # Se modifica la lista de acuerdo a la posicion del elemento
"""

# Ejemplo
vocales = ["a", "e", "i", "o", "u"]
print(f"lista inicial: {vocales[0:2]}")
vocales[0:2] = ["x", "y"]
print(f"\nlista modificada: {vocales[0:2]}")
print()

#Otro ejemplo
print("\nOtro ejemplo: ")
print("Modificando vocales[1] = 'x'")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[1] = "x"
print(f"Lista vocales: {vocaales}")


print("\nModificando vocales[1] = '2'")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[1] = 2
print(f"Lista vocales: {vocaales}")


print("\nModificando vocales[-1] = 'x'")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[-1] = "x"
print(f"Lista vocales: {vocaales}")


print("\nModificando vocales[2:4] = ['x', 'y']")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[2:4] = ["x", "y"]
print(f"Lista vocales: {vocaales}")


print("\nModificando vocales[1:3] = ['x', 'y']")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[1:3] = ["x", "y"]
print(f"Lista vocales: {vocaales}")


print("\nModificando vocales[1:3] = ['x', 'y', 'z']")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[1:3] = ["x", "y", "z"]
print(f"Lista vocales: {vocaales}")


print("\nModificando vocales[:2] = ['x', 'y', 'z']")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[:2] = ["x", "y", "z"]
print(f"Lista vocales: {vocaales}")


print("\nModificando vocales[0:3] = ['x', 'y']")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[0:3] = ["x", "y"]
print(f"Lista vocales: {vocaales}")


print("\nModificando vocales[0:3] = 'x', 'y'")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[0:3] = "x", "y"
print(f"Lista vocales: {vocaales}")


print("\nModificando vocales[:] = 'x'")
vocaales = ["a", "e", "i", "o", "u"]
print(f"\nLista vocales: {vocaales}")
vocaales[:] = "x"
print(f"Lista vocales: {vocaales}")













