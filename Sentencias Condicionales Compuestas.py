"""
Sentencias condicionales compuestas -> if (condicion):
                                           Instruccion
                                       else:
                                           Instruccion
"""

# Ejemplo
num_uno = 10
if num_uno == 5:
    print("El numero es cinco")
else:
    print("El nummero no es cinco")
print("Fin." + "\n")


# Otro ejemplo
print("Sistema para calcular el promedio de un alumno:")
nombre = input("¿Cual es tu nombre? : ")
quimica = float(input(nombre + " ¿Cual es tu promedio en quimica? : "))
matematicas = float(input(nombre + " ¿Cual es tu promedio en matematicas? : "))
biologia = float(input(nombre + " ¿Cual es tu promedio en biologia? : "))
promedio = (quimica + matematicas + biologia)/3


if promedio >= 6.0:
    print("Felicidades " + nombre + " 'aprobaste' con un promedio de :", round(promedio,2))# sirve para aproximar decimales->round(variable, numero_decimales_a_redondear)
else:
    print("Malas noticias " + nombre + " 'no aprobaste', tu promedio es muy bajo : ", round(promedio,2))
print("Fin.")


