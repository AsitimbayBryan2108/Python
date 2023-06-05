consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213, 400), 'tarifa': 65}
    }
}

tarifa_coca_quito = consumo_energia['Coca Codo Sinclair']['Quito']['tarifa']
consumos_coca_quito = consumo_energia['Coca Codo Sinclair']['Quito']['consumos']

print(consumo_energia['Coca Codo Sinclair']['Quito']['consumos'][3])
print(consumo_energia['Coca Codo Sinclair']['Quito']['consumos'][11])
print(consumo_energia['Coca Codo Sinclair']['Quito']['tarifa'])
print(tarifa_coca_quito * consumos_coca_quito[11])

print(consumos_coca_quito)

consumo = 0
for c in consumos_coca_quito:
    consumo += c

print('Consumo total:', consumo)