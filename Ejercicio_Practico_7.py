# Ejercicio Practico 7

menu = "Inversion de cadena"
print(f"{menu.center(40, '=')}\n")

cadena = input("Por favor introduce una cadena de texto: ")
cad = ""

for c in cadena:
    cad = c + cad

print(f"La cadena invertida es: {cad} \n\n")


#Realice un programa que enumere los paises de la siguiente lista
print("Otro ejercicio: ")
paises = ['Canada', 'USA', 'Mexico', 'Australia']
num = [1,2,3,4]
print()


for i,co in enumerate(paises):
        print(f" {i}. {co}")
