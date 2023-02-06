# Cadena de caracteres
mensaje = "Hola"
mensaje += " " #Sumar contenido dentro de la variable +=
mensaje += "Ernesto" #Sumar contenido dentro de la variable +=
print(mensaje + "\n")


# Concatenacion
print("Concatenacion: ")
mensaje_2 = "Hola"
espacio = " "
nombre = "Ernesto"
print(mensaje_2 + espacio + nombre+"\n")

print("Concatenación de caracteres con numeros:")
numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado) #Conversion del valor numero a string
print("El resultado de la suma es: " + resultado + "\n")

# Otra forma de concatenación:
# Ejemplo solo texto sin variables
ej = str(3 * 'un' + 'ium' + '\n') # 3 * 'str' -> En la concatenacion repite la cadena que esta al lado
print(ej)


# Busqueda con el metodo(find) -> Obtener subcadenas para obtener la posicion
print("Busqueda:")
mensaje_3 = "Hola Ernesto"
buscar_subcadena = mensaje_3.find("Ernesto")
buscar_subcadena = str(buscar_subcadena)
print(buscar_subcadena + "\n")

# Extraccion -> posicion a extraer [1:8]// siempre la posicion empieza con 0
print("Extraer: ")
mensaje_4 = "Hola Ernesto"
extraer_subcadena = mensaje_4[1:8]
extraer_subcadena = str(extraer_subcadena)
print(extraer_subcadena + "\n")

print("Otro ejemplo de extraccion:")
ext = 'Me llamo Brihan'
print(ext[:2] + '\n') # se obtenie lo que esta hacia atras desde la posicion 2 en este caso

print('Otra forma puede ser:')
print(ext[2:] + '\n') # se obtenie lo que esta hacia adelante desde la posicion 2 en este caso


print('Otra forma puede ser:')
print(ext[:2] + ext[2:] + '\n')# se concatena de acuerdo a la posicion de las cadena de texto

# Comparacion (==) -> se utiliza para comparar dos cadenas de caracteres
print("Comparacion:")
mensaje_cinco = "Hola"
mensaje_seis = "Hola"
print(mensaje_cinco == mensaje_seis) # == comparacion







