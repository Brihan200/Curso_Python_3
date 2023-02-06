# Sentencias Break y Continue

# Break -> Se utiliza para detener la ejecucion de una iteracion y salir de ella
# ej.
print("While con la sentencia break \n")
contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        break # Se detiene la ejecucion
    
    print("Valor actual de la variable ", contador)
    
print("Fin del programa, la sentencia break se ha ejecutado. \n")



# Continue -> Permite detener la interaccion actual y volver a empezar
# ej.
print("\nWhile con la sentencia continue \n")
contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print("Valor actual de la variable: ", contador)

print("Fin del programa, la sentencia continue se ha ejecutado.")
