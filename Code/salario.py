#Calcular la utilidad que un trabajador recibe del reparto anual de utilidades 
# si éste se le asigna como un porcentaje de su salario mensual que depende de su antigüedad en la empresa, 
# de acuerdo con la siguiente tabla:
#Tiempo | Utilidad
#Menos de 1 año | 5% del salario
#1 año o más y menos de 2 años | 7% del salario
#2 años o más y menos de 5 años | 10% del salario
#5 años o más y menos de 10 años | 15% del salario
#10 años | 20% del salario.

antiguedad=int(input("Ingresa años trabajados:"))
salario=int(input("Ingresa el valor de salario:"))
utilidades=0
if antiguedad<1:
    utilidades=0.05*salario
elif antiguedad>=1 and antiguedad<2:
    utilidades=0.07*salario
elif antiguedad>=2 and antiguedad<5:
    utilidades=0.1*salario
elif antiguedad>=5 and antiguedad<10:
    utilidades=0.15*salario
elif antiguedad>=10:
    utilidades=0.2*salario
print("El valor de utilidades:", utilidades)
