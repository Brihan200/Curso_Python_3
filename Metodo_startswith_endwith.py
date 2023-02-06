# Metodo startswith() - endswith()

"""
* startswith() -> Se utiliza para comprobar si una cadena de caracteres comienza con una subcadena particular // Arroja un booleano(True/False)
                Sintaxis: nombre_variable.startswith("substring", int(posicion_inicial), int(posicion_final))
                
* endswith()   -> Se utiliza para comprobar si una cadena de caracteres termina con una subcadena particular // Arroja un booleano(True/False)
                Sintaxis: nombre_variable.endswith("substring", int(posicion_final), int(posicion_inicial))
"""

# Ejemplo startswith()
string = "Diana se peina sola"
print(string.startswith("se", 6, 7))

print()

# Ejemplo endswith
sttring = "Hola mundo"
print(sttring.endswith("o", 9 , 10))

print()

#Otro ejemplo
st = "Diana se peina sola"
resultado = 0
starts_with = "Ejemplos con startswith(): "
ends_with = "Ejemplos con endswith(): "

print(f"\n{starts_with.rjust(50, '=')}")

resultado = st.startswith("D")
print(f"\n{st} comienza con la subcadena D: {resultado}")

resultado = st.startswith("d")
print(f"\n{st} comienza con la subcadena d: {resultado}")

resultado = st.startswith("Diana")
print(f"\n{st} comienza con la subcadena Diana: {resultado}")

resultado = st.startswith("se", 6)
print(f"\n{st} comienza con la subcadena se, desde la posicion 6 : {resultado}")

resultado = st.startswith("se", 6, 7)
print(f"\n{st} comienza con la subcadena se, desde la posicion 6 hasta la posicion 7: {resultado}")




print(f"\n{ends_with.rjust(50, '=')}")

resultado = st.endswith("A")
print(f"\n{st} termina con la subcadena A: {resultado}")

resultado = st.endswith("a")
print(f"\n{st} termina con la subcadena a: {resultado}")

resultado = st.endswith("sola")
print(f"\n{st} termina con la subcadena sola: {resultado}")

resultado = st.endswith("sola", 10)
print(f"\n{st} termina con la subcadena sola desde la posicion 10: {resultado}")

resultado = st.endswith("s", 9, 14)
print(f"\n{st} termina con la subcadena s desde la posicion 9 hasta la posicion 14: {resultado}")










