# Metodo count()

"""
* count() -> Sirve para conocer la cantidad de veces que aparece una cadena o caracter especifico dentro de un texto
             Sintaxis: nombre_variable.count("substring", int(ubicacion_posicion_inicio), int(ubicacion_posicion_fin))
"""

#Ejemplo
cadena = "Hola mundo"
print(cadena.count(""))

print()

# Otro ejemplo

string = "mi mama me mima"
print(string.count("m", 0, 8))

print()

# Otro ejemplo
print("Otro ej: ")
sttring = "mi mama me mima"
contador = 0

print(sttring.center(40, "="))

contador = sttring.count("M")
print(f"\nla letra 'M' se encontro {contador} veces en la cadena: {sttring}")

contador = sttring.count("m")
print(f"\nla letra 'm' se encontro {contador} veces en la cadena: {sttring}")

contador = sttring.count("mama")
print(f"\nla palabra 'mama' se encontro {contador} veces en la cadena: {sttring}")

contador = sttring.count("me mima")
print(f"\nla oracion 'me mima' se encontro {contador} veces en la cadena: {sttring}")

contador = sttring.count("ma")
print(f"\nla palabra me 'ma' se encontro {contador} veces en la cadena: {sttring}")

contador = sttring.count("m", 13)
print(f"\nla letra 'm' se encontro {contador} veces, desde la posicion 13 en la cadena: {sttring}")

contador = sttring.count("m", 100)
print(f"\nla letra 'm' se encontro {contador} veces, desde la posicion 100 en la cadena: {sttring}")

contador = sttring.count("m", -3)
print(f"\nla letra 'm' se encontro {contador} veces, desde la posicion -3 en la cadena: {sttring}")

contador = sttring.count("m", 3, 7)
print(f"\nla letra 'm' se encontro {contador} veces, desde la posicion 3 hasta la posicion 7 en la cadena: {sttring}")

contador = sttring.count("m", 100, 100)
print(f"\nla letra 'm' se encontro {contador} veces, desde la posicion 100 hasta la posicion 100 en la cadena: {sttring}")

contador = sttring.count("m", -4, -1)
print(f"\nla letra 'm' se encontro {contador} veces, desde la posicion -4 hasta la posicion -1 en la cadena: {sttring}")
