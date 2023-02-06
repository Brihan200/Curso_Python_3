"""
Sentencias condicional multiple -> if(condicion):
                                       Intruccion
                                   elif(condicion):
                                       Instruccion
                                   else:
                                       Instruccion
                                   
"""

# Ejemplo
num_uno = 1
if num_uno == 1:
    print("El numero es UNO")
elif num_uno ==2:
    print("El numero es DOS")
else:
    print("El numero se desconoce")
    
print("Fin." + "\n")

# Otro Ejemplo
# Convertir de numeros a letras -> solo hasta el numero 5
print("¡¡¡Convertidor de numeros a letras!!!")
print("====================================")
convertir = int(input("¿Cual es el numero que deseas convertir?: "))

if convertir == 1:
    print("El numero es 'Uno'")
elif convertir == 2:
    print("El numero es 'Dos'")
elif convertir == 3:
    print("El numero es 'Tres'")
elif convertir == 4:
    print("El numero es 'Cuatro'")
elif convertir == 5:
    print("El numero es 'Cinco'")
else:
    print("El numero es mayor que 5, no aplica para este ejercicio")
print("Fin.")


