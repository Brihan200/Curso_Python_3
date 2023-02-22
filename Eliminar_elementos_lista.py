# Eliminar elementos de una lista con el metodo pop()

"""
* pop() -> Nos permite eliminar el ultimo elemento o un elemento especifico de una lista

Sintaxis: nombre_lista.pop(posicion) # posicion -> valor_entero(positivo o negativo)
"""

#Ejemplo
vocales = ["a", "e", "i", "o", "u"]
print(vocales)
vocales.pop()
print(f"Lista con ultimo elemento eliminado: {vocales} \n")

# Otro ejemplo
print("Otro ejemplo: ")
vocal = ["a", "e", "i", "o", "u"]
print(f"Lista: {vocal}")
print(f"Elemento eliminado: {vocal.pop()}")
print(f"Lista: {vocal}")

vocal = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocal}")
print(f"Elemento eliminado en la posicion 2: {vocal.pop(2)}")
print(f"Lista: {vocal}")

vocal = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocal}")
print(f"Elemento eliminado en la posicion 0: {vocal.pop(0)}")
print(f"Lista: {vocal}")

vocal = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocal}")
print(f"Elemento eliminado en la posicion -2: {vocal.pop(-2)}")
print(f"Lista: {vocal}")

vocal = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocal}")
print(f"Elemento eliminado en la posicion 5 : {vocal.pop(5)}") # Generar el error
print(f"Lista: {vocal}")
