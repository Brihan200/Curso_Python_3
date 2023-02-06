# Ejercicio practico

print("===============")
print("Sistema de calculo de vacaciones de la empresa Rappi: ")
print("===============" + "\n")

nombre_trabajador = input("Hola por favor indique su nombre : ")
nombre_trabajador = nombre_trabajador.upper()
clave_depa = int(input("Por favor indique el departemento al que trabaja: (1 para Atencion al cliente" + ", 2 para logistica, 3 para Gerencia) : "))
anos_trabajados = int(input("Por favor indique los años trabajados: "))
print("\n")

if clave_depa == 1:
    print("Atencion al cliente: ")
    
    if anos_trabajados == 1 and anos_trabajados < 2:
        print("El empleador " + nombre_trabajador + " recibe 6 dias de vacaciones :)")
    elif anos_trabajados >= 2 and anos_trabajados <= 6:
        print("El empleador " + nombre_trabajador + " recibe 14 dias de vacaciones :)")
    elif anos_trabajados >= 7:
        print("El empleador " + nombre_trabajador + " recibe 20 dias de vacaciones :)")
    else:
        print("El empleador no tiene derecho a vacaciones")
        
elif clave_depa == 2:
    print("Logistica: ")
    
    if anos_trabajados == 1 and anos_trabajados < 2:
        print("El empleador " + nombre_trabajador + " recibe 7 dias de vacaciones :)")
    elif anos_trabajados >= 2 and anos_trabajados <= 6:
        print("El empleador " + nombre_trabajador + " recibe 15 dias de vacaciones :)")
    elif anos_trabajados >= 7:
        print("El empleador " + nombre_trabajador + " recibe 22 dias de vacaciones :)")
    else:
        print("El empleador no tiene derecho a vacaciones")
        
elif clave_depa == 3:
    print("Gerencia: ")
    
    if anos_trabajados == 1 and anos_trabajados < 2:
        print("El empleador " + nombre_trabajador + " recibe 10 dias de vacaciones :)")
    elif anos_trabajados >= 2 and anos_trabajados <= 6:
        print("El empleador " + nombre_trabajador + " recibe 20 dias de vacaciones :)")
    elif anos_trabajados >= 7:
        print("El empleador " + nombre_trabajador + " recibe 30 dias de vacaciones :)")
    else:
        print("El empleador no tiene derecho a vacaciones")
        
else:
    print("La clave del departamento no existe, vuelve a intentarlo")
print("Fin.")



