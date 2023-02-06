# Sentencias condicionales

"""
Simples -> if (condicion):
               instruccion  # Identación
"""

edad = int(input("Indique por favor su edad: "))

if edad >= 18:
    print("Es mayor de edad" + "\n")
print("Es menor de edad" + "\n")


# Otro ejemplo
num_uno = 10

if num_uno == 5:
    print("El numero es cinco", "\n")
print("Fin", "\n")

# Otro ejemplo
print("Sistema para calcular el promedio de un alumno:")
nombre = input("¿Cual es tu nombre? : ")
quimica = float(input(nombre + " ¿Cual es tu promedio en quimica? : "))
matematicas = float(input(nombre + " ¿Cual es tu promedio en matematicas? : "))
biologia = float(input(nombre + " ¿Cual es tu promedio en biologia? : "))
promedio = (quimica + matematicas + biologia)/3

if promedio >= 6.0:
    print("Felicidades " + nombre + " 'aprobaste' con un promedio de :", int(promedio))
print("Malas noticias " + nombre + " 'no aprobaste', tu promedio es muy bajo : ", int(promedio))
print("Tipos de datos.py")



























