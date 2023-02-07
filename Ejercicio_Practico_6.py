# Ejercicio Practico #6

titulo = "Eliminar palabra de una cadena"
print(titulo.center(50, "="), "\n")

cadena = input("Por favor introduce una cadena de texto: ")
palabra = input("Por favor elimina una palabra de la cadena: ")
sub = ""

indice = cadena.find(palabra)
sub = cadena[0: indice] + cadena[indice + len(palabra) + 1: ]

print(f"Cadena resultante: {sub}")

