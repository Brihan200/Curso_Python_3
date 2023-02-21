# Insertar elementos en una lista con el metodo insert()

"""
insert() -> Nos permite indicar la posicion exacta donde se va a insertar el nuevo elemento

Sintaxis: nombre_lista.insert(posicion(valor_entero), nuevo_elemento)

"""

#Ejemplo
print("Ejemplo")

# Posicion: 0    1    2    3
letras = ["a", "b", "c", "d"]
# Elemento: 1    2    3    4

print(letras)
letras.insert(2, "e") # Si ya a un valor en la posicion de la lista, inserta el elemento y corre las posiciones restantes
print(letras, "\n")


# Otro ejemplo
ej = "Otro ejemplo"
print(ej.center(20, "="))
letters = ["b", "d", "f", "g"]
print(f"\nLista: {letters}")

print("\nInsertando 'a' en posicion 0 ")
letters.insert(0, "a")
print(f"Lista: {letters}")

print("\nInsertando 'c' en posicion 2 ")
letters.insert(2, "c")
print(f"Lista: {letters}")

print("\nInsertando 'e' en posicion 4 ")
letters.insert(4, "e")
print(f"Lista: {letters}")

print("\nInsertando 'z' en posicion 100 ")
letters.insert(100, "z")
print(f"Lista: {letters}")



