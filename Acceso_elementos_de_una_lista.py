# Acceso a los elementos de una lista

#Ej
marcas = ["Apple", "Samsung", "Xiaomi", "Huawei"] # Siempre se empieza desde la posicion 0
print(len(marcas)) # len()-> saber la longitud de las listas o variables
print("\n", marcas[1:3]) # Conocer el valor de un elemento de la lista por medio de la posicion ya sea positiva o negativa

#Otro ejemplo
print("\n\nOtro ejemplo: \n")
print("Accediendo a las posiciones de una lista")

print(f"\nLista completa: {marcas}")
print(f"\n¿Cuantos elementos tiene la lista?: {len(marcas)}")
print(f"\nmarcas[1]: {marcas[1]}")
print(f"\nmarcas[3]: {marcas[3]}")
print(f"\nmarcas[-1]: {marcas[-1]}")
print(f"\nmarcas[-3]: {marcas[-3]}")
print(f"\nmarcas[1:3]: {marcas[1:3]}")
print(f"\nmarcas[:2]: {marcas[:2]}")
print(f"\nmarcas[1:]: {marcas[1:]}")
print(f"\nmarcas[:]: {marcas[:]}")

