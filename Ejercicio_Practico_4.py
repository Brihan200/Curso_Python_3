# Calculadora

print("============================")
print("Calculadora")
print("============================" + "\n")

print("Opciones: \n","1. Suma \n","2. Resta \n","3. Multiplicacion \n", "4. Division \n", "5. Division Entera \n"
      ,"6. Exponente \n", "7. Modulo \n")
opcion = int(input("Por favor eliga una opcion: "))

if opcion == 1:
    
    num = int(input("Por favor indica un numero: "))
    num += int(input("Por favor indica otro numero: "))
    print("\nLa suma es :", num)
    
elif opcion == 2:
    
    num = int(input("Por favor indica un numero: "))
    num -= int(input("Por favor indica otro numero: "))
    print("\nLa resta es :", num)
    
elif opcion == 3:
    
    num = int(input("Por favor indica un numero: "))
    num *= int(input("Por favor indica otro numero: "))
    print("\nLa multiplicacion es :", num)
    
elif opcion == 4:
    
    num = float(input("Por favor indica un numero: "))
    num /= float(input("Por favor indica otro numero: "))
    print("\nLa division es :", num)
    
elif opcion == 5:
    
    num = float(input("Por favor indica un numero: "))
    num //= float(input("Por favor indica otro numero: "))
    print("\nLa division entera es :", num)
    
elif opcion == 6:
    
    num = int(input("Por favor indica un numero: "))
    num **= int(input("Por favor indica otro numero: "))
    print("\nEl exponente es :", num)
    
elif opcion == 7:
    
    num = int(input("Por favor indica un numero: "))
    num %= int(input("Por favor indica otro numero: "))
    print("\nEl modulo es :", num)
    
else:
    print("Opcion no valida")
    
print("Fin.")

