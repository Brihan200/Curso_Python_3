# Entrada de datos en python -> input()

print('Hola Brihan vamos a realizar una suma:')
palabra = input("Indica por favor tu apellido: ")
primer_valor = int(input("Porfavor introduzca el primer valor entero: "))
segundo_valor = int(input("Porfavor introduzca el segundo valor entero: "))
numero_flotante = float(input("Porfavor introduzca un valor flotante: "))
resultado = primer_valor + segundo_valor
print("El resultado es: " + str(resultado) + '\n' ,'Su apellido es :',palabra)
print("El numero flotante es : " + str(numero_flotante))

print("\n")

# Otro ejercicio de input
nombre = input("Introduzca por favor su nombre: ")
print("Hola " + nombre + ", vamos a realizar una multiplicacion :")
num_uno = int(input('Por favor introduce el primer valor: '))
num_dos = int(input('Por favor introduce el segundo valor: '))
result = num_uno * num_dos
print(nombre + ' el resultado de la multiplicación es :', result)

