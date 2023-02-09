# Clase Range

"""
* range -> Genera secuencia de numeros inmutables, es decir que no se pueden modificar, estas secuencias se generan a partir de un rango previamente establecido
           por lo general se utiliza en el ciclo for

           Sintaxis: range(start,stop, step)      // stop: es un valor entero que indica el numero hasta el cual se va a generar la secuencia de numeros
                                                  // start: es un valor entero que indica el numero del cual comenzara a generar la secuencia de numeros
                                                  // step: es un valor entero que indica el incremento o decremento(+,-) de la sucesion numerica de un numero y el siguiente

"""

#Ej stop
range(10) #(stop)/ Numero range: -> Comienza siempre empieza con el 0

#Ej start-stop
range(5, 11)

#Ej start-stop-step
range(0, 11, 2)

"""
Sintaxis bucle for con range():

    for variable in range(start,stop,step):
        instruccion
        instruccion
"""

#Ej con for

for indice in range(1,5):
    print(indice)

print("Fin del programa \n")

print()


# Otro ejemplo
print("Otro ejemplo: ")

for indicce in range(10, 0, -1): # Decremento del step
    print(indicce)

print("Fin del ejemplo")

