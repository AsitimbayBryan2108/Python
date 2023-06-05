#1.8. Un año es bisiesto si es divisible por 4 y no es por 100, o si es divisible por 400. 
# Escribe un programa que lea un año y devuelva si es bisiesto o no.

bisiesto=int(input("Ingrese un año:"))

if bisiesto%4==0 and bisiesto%100!=0 or bisiesto%400==0:
    print("El año",bisiesto,"si es bisiesto")
else:
    print("El año",bisiesto,"no es bisiesto")