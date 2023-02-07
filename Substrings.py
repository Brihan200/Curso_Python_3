# Subtrings

"""
* Substring -> Es una sucesion de caracteres dentro de una cadena principal
               Ej: "Aprendiendo Python" -> Cadena Principal
                   "Python"             -> Subcadena

               Sintaxis: nombre_variable[inicio : final: saltos] // los valores inicio y final debe ser enteros // los saltos pueden ser positivos y negativos
               
               inicio -> Establece el indice donde se iniciara la subcadena
               final ->  Establece el indice donde se terminara la subcadena
               saltos -> Establece el numero de saltos que realizara el indice para generar la subcadena
"""


#Ej
string = "0123456789"
print(string[1:6:2]) # Indice-Posicion

print()

#Otro ejemplo
print("Otro ejemplo: \n \n")
sttring = '0123456789'
substring = ""

print(f"cadena principal: {sttring}")

substring = sttring[0]
print(f"\nSubcadena con indice en la posicion [0] es: {substring}")

substring = sttring[5]
print(f"\nSubcadena con indice en la posicion [5] es: {substring}")

substring = sttring[-4]
print(f"\nSubcadena con indice en la posicion [-4] es: {substring}")

substring = sttring[0:3]
print(f"\nSubcadena con indices en las posiciones [0:3] es: {substring}")

substring = sttring[:3]
print(f"\nSubcadena con indices en las posiciones [:3] es: {substring}")

substring = sttring[5:]
print(f"\nSubcadena con indices en las posiciones [5:] es: {substring}")

substring = sttring[-4:-1]
print(f"\nSubcadena con indices en las posiciones [-4:-1] es: {substring}")

subtring = sttring[:]
print(f"\nSubcadena con indices en las posiciones [:] es: {substring}")

substring = sttring[1:6:2]
print(f"\nSubcadena con indices en las posiciones y salto [1:6:2] es: {substring}")

substring = sttring[::3]
print(f"\nSubcadena con indices en las posiciones y salto [::3] es: {substring}")
