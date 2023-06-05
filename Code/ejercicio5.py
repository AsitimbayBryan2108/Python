#Calcular el mayor de tres números enteros introducidos por teclado.

num1= int(input("Ingrese primer numero entero:"))
num2= int(input("Ingrese segundo numero entero:"))
num3= int(input("Ingrese tercer numero entero:"))

if num1>num2:
    print("Primer numero es mayor")
elif num2>num3:
    print("Segundo numero es mayor")
elif num3>num1:
    print("Tercer numero es mayor")
else:
    print("Todos son iguales")




