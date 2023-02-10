# Ejercicio Practico #9

menu = 'Ejercicio'
print(f"{menu.center(50,'=')} \n")

palabra = input("Por favor ingrese una frase: ")
caracter = input("Por favor ingrese un caracter para detener el ciclo: ")

print()


for p in palabra:
    if p.lower() == caracter.lower():
        break
    elif p.lower() == 'a':
        continue
    elif p.lower() == 'e':
        continue
    elif p.lower() == 'i':
        continue
    elif p.lower() == 'o':
        continue
    elif p.lower() == 'u':
        continue
    print(p, end="")
