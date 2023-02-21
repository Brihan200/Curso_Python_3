# Agregar elementos a una lista con el metodo append()

"""
append() -> permite agregar elementos

Sintaxis: nombre_lista.append(nuevo_elemento)

"""

letras = ["a", "b" , "c", "d"]
print(f"Lista inicial: {letras}")
#nuevo elemento append
letras.append("e")
letras.append("f")
print(f"Lista con nuevo elemento: {letras}")

print(f"\nAgregando 3 elementos a la lista: {letras}")
print(f"Lista : {letras}")
#nuevo elemento append
letras.append("g")
letras.append("h")
letras.append("i")
print(f"Lista con 3 elementos: {letras}")

print(f"\nAgregando 3 elementos de distinto tipo de dato a la lista: {letras}")
print(f"Lista : {letras}")
#nuevo elemento append
letras.append(5)
letras.append(2.3)
letras.append(True)
print(f"Lista con 3 elementos distintos: {letras}")
