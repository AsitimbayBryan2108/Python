#Llenar un vector de 20 elementos, imprimir la posición 
# y el valor del elemento mayor almacenado en el vector. 
# Suponga que todos los elementos del vector son diferentes.

lista1=[]
n=15
mayor=0

for i in range(n):
    venta= int(input('Ingrese el monto de venta:'))
    lista1.append(venta)
    if venta > mayor:
        mayor=venta
        positivo=i
print ("el numero mayor es:",mayor ,"y la posicion es:",positivo)