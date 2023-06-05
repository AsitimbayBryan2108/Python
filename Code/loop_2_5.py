# Leer 10 números e imprimir solamente los números positivos.

n = 5
for i in range(n):
    num = int(input('Ingrese numero: '))
    if num > 0:
        print(num)
    else:
        print('Ingrese numeros positivos')

