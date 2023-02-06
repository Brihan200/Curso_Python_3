#Metodo center ljust- rjust

"""
* center() -> Nos permite centrar un string
             Sintaxis: nombre_variable.center(numero_entero, "caracter")
             
* ljust() -> Nos permite alinear un string a la izquierda añadiendo espacios o caracteres segun se indique
             Sintaxis: nombre_variable.ljust(numero_entero, "caracter")

* rjust() -> Nos permite alinear un string a la derecha añadiendo espacios o caracteres segun se indique
             Sintaxis: nombre_variable.rjust(numero_entero, "caracter")

"""

# Ejemplo center()
print("Center(): ")
string = 'centro'
print(string.center(10, "=")) # El numero_entero debe ser mayor que la longitud de la variable // El caracter reemplaza los espacios vacios que genera

print()

# Ejemplo ljust()
print("Ljust(): ")
ljustt = "izquierda"
print(ljustt.ljust(15, "="))

print()

# Ejemplo rjust()
print("Rjust(): ")
rjustt = "derecha"
print(rjustt.rjust(15, "="))

print()

# Otro ejemplo
sttring = "Menú"

print("Metodos con espacios: ")
print(sttring.center(20))
print(sttring.ljust(20))
print(sttring.rjust(20))

print("\nMetodos con caracter: ")
print(sttring.center(20, "="))
print(sttring.ljust(20, "="))
print(sttring.rjust(20, "="))

print("\nVariable Modificada: ")
sttring = sttring.center(10, "=")
print(sttring)


