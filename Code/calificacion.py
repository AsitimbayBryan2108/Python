#suponga que se tiene un conjunto de calificaciones de un grupo de 40 alumnos.
#realizar un algoritmo y programa para calcular la calificiacion media
#y la calificacion mas baja de todo el grupo.
n= int(input("Ingrese estudiantes:"))
suma=0
for i in range(n):
    nota=int(input("Ingrese venta:"))
    suma= suma+nota

print("Suma total:", suma)
media_aritmetica =suma/n
print("La media aritmetica es:", media_aritmetica)
nota<7
print ("la nota mas baja es:",nota)