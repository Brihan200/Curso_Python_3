# Metodos strip(), rstrip(), lstrip()

"""
* strip() -> Se utiliza para eliminar caracteres especificos al inicio y al final de una cadena de caracteres//solo elimina espacios en blanco y saltos de linea si no se especifica
            Sintaxis: cadena.strip()-> "Hola ernesto ".strip("o")
            
* rstrip() -> Se utiliza para eliminar unicamente caracteres al final de una cadena// solo elimina espacios en blanco y salto de linea si no se especifica
            Sintaxis: cadena.rstrip() -> " Hola Ernesto ".rstrip("o")

* lstrip() -> Se utiliza para eliminar unicamente caracteres al inicio de una cadena// solo elimina espacios en blanco y saltos de linea si no se especifica
            Sintaxis: cadena.lstrip() -> " Hola Ernesto ".lstrip("H")
"""

# strip() ej:
print("* strip: ")
cadena = " Hola Brihan "
cadena = cadena.strip("b n H")
print(cadena + "\n")

# Otro ej:
cadena_2 = "\t Hola Ernesto \n"
print(cadena_2)
cadena_2 = cadena_2.strip("s tHo \t\n")
print(cadena_2 + "\n")

# rstrip():
print("* rstrip: ")
cadena_3 = " Hola Brihan "
cadena_3 = cadena_3.rstrip(" nH")
print(cadena_3 + "\n")

# Otro ej:
cadena_4 = "\t Hola Ernesto \n"
print(cadena_4)
cadena_4 = cadena_4.rstrip("s t H o \t\n")
print(cadena_4 + "\n")

# lstrip():
print("* lstrip: ")
cadena_5 = " Hola Brihan "
cadena_5 = cadena_5.lstrip(" nH")
print(cadena_5 + "\n")

# Otro ej:
cadena_6 = "\t Hola Ernesto \n"
print(cadena_6)
cadena_6 = cadena_6.lstrip("s t H o \t\n")
print(cadena_6)


