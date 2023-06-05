# Leer 5 números e imprimir cuantos 
# son positivos, cuantos negativos y cuantos neutros.

positivos = 0; negativos =0;neutros=0

for i in range(5):
    num = int(input('Ingrese numero: '))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        neutros += 1

print('Total positivos:', positivos)
print('Total negativos:', negativos)
print('Total neutros:', neutros)