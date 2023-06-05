# Calcular el promedio de un alumno que tiene 7 calificaciones en la materia de Cálculo.

# n1 = int(input('Ingrese nota 1: '))
# n2 = int(input('Ingrese nota 2: '))
# n3 = int(input('Ingrese nota 3: '))
# n4 = int(input('Ingrese nota 4: '))
# n5 = int(input('Ingrese nota 5: '))
# n6 = int(input('Ingrese nota 6: '))
# n7 = int(input('Ingrese nota 7: '))

# suma = (n1+n2+n3+n4+n5+n6+n7)
# promedio = suma/7

# print('Promedio:', promedio)

n = 7
suma = 0
for i in range(n):
    nota = float(input('Ingrese nota ' + str(i) + ': '))
    suma = suma + nota

promedio = suma/n
print('Promedio:', promedio)
