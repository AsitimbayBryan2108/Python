#1.7. Determinar en que estado está el agua en función de su temperatura. 
# Si es negativa el estado será sólido, si es menor que 100 será líquido y si es mayor que 100 será gas. 
# Pedir al usuario el valor de la temperatura.

temp=int(input("Ingrese un valor de temperatura:"))

if temp<0:
    print("Su estado es solido")
elif temp<100:
    print("Su estado es liquido")
else:
    print("Su estado es gaseoso")