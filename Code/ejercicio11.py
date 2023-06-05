#Solicitar al usuario la inicial del día de la semana y mostrar el nombre del día completo. 
# La letra inicial puede ser mayúscula o minúscula. 
# Usar la x para el miércoles.

dia= input("Ingrese la inicial del dia:")
dia=dia.lower()
#print=dia.upper()
if dia=="l":
    print("Lunes")
elif dia=="m":
    print("Martes")
elif dia=="x":
    print("Miercoles")
elif dia=="j":
    print("Jueves")
elif dia=="v":
    print("Viernes")
elif dia=="s":
    print("Sabado")
elif dia=="d":
    print("Domingo")
else:
    print("Dia equivocado")
    
