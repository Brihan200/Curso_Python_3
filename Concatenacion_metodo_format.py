# Metodo format()

"""
format() -> Permite mostrar los valores contenidos en una variable y utilizarlos dentro de una cadena de caracteres, sustituyendo el nombre de la variable con {}
            no importa si son de tipo String o Int o Float
"""

#Ej. 1 forma
nombre = "Carlos"
edad = 22

print("Hola {} tienes {} años.".format(nombre, edad)) # format()

#Ej. 2 forma
print("Hola {nombre_2} tienes {edad_2} años.".format(nombre_2 = "Camilo", edad_2 = 25))

#Ej. 3 forma
nombre_3 = 'Brihan'
edad_3 = 29

print("Hola {0} tienes {1} años.".format(nombre_3, edad_3)) # Posicion desde 0
