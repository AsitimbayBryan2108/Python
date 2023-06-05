consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 432, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32), 'tarifa': 84}
    },
    'Sopladora':{
        'Guayaquil': {'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321), 'tarifa': 55},
        'Quito': {'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587), 'tarifa': 79},
        'Loja': {'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32), 'tarifa': 32},
    },
}
#COCA CODO GUAYAQUIL
consumos_coca_codo_guayaquil = consumo_energia['Coca Codo Sinclair']['Guayaquil']['consumos']
tarifa_coca_codo_guayaquil = consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa']
consumo_gy= 0
for c in consumos_coca_codo_guayaquil:
    consumo_gy += c
consumos_totales_guayaquil = (consumo_gy * tarifa_coca_codo_guayaquil)
print("Los consumos totales de Coca Codo en Guayaquil son:", consumos_totales_guayaquil)
#COCA CODO QUITO
consumos_coca_codo_quito = consumo_energia['Coca Codo Sinclair']['Quito']['consumos']
tarifa_coca_codo_quito = consumo_energia['Coca Codo Sinclair']['Quito']['tarifa']
consumo_quito= 0
for q in consumos_coca_codo_quito:
    consumo_quito += q
consumos_totales_quito = (consumo_quito * tarifa_coca_codo_quito)
print("Los consumos totales de coca codo en Quito son:", consumos_totales_quito)
#SOPLADORA GUAYAQUIL
consumos_sopladora_guayaquil = consumo_energia['Sopladora']['Guayaquil']['consumos']
tarifa_sopladora_guayaquil = consumo_energia['Sopladora']['Guayaquil']['tarifa']
consumo_sopladora_gy= 0
for b in consumos_sopladora_guayaquil:
    consumo_sopladora_gy += b
consumos_totales_guayaquil_sopladora = (consumo_sopladora_gy * tarifa_sopladora_guayaquil)
print("Los consumos totales de la sopladora en Guayaquil son:", consumos_totales_guayaquil_sopladora)
#SOPLADORA QUITO
consumos_sopladora_quito = consumo_energia['Sopladora']['Quito']['consumos']
tarifa_sopladora_quito = consumo_energia['Sopladora']['Quito']['tarifa']
consumo_sopladora_qui= 0
for d in consumos_sopladora_quito:
    consumo_sopladora_qui += d
consumos_totales_sopladora_quito = (consumo_sopladora_qui * tarifa_sopladora_quito)
print("Los consumos totales de la sopladora en Quito son:", consumos_totales_sopladora_quito)
#SOPLADORA LOJA 
consumos_sopladora_loja = consumo_energia['Sopladora']['Loja']['consumos']
tarifa_sopladora_loja = consumo_energia['Sopladora']['Loja']['tarifa']
consumo_sopladora_loj= 0
for e in consumos_sopladora_loja:
    consumo_sopladora_loj += e
consumos_totales_sopladora_loja = (consumo_sopladora_loj * tarifa_sopladora_loja)
print("Los consumos totales de la sopladora en Loja son:", consumos_totales_sopladora_loja)
#Diccionario 2
consumo_energia2 = {
    'Guayaquil':{
        'Coca Codo Sinclaire': [consumos_totales_guayaquil],
        'Sopladora': [consumos_totales_guayaquil_sopladora]
    },
    'Quito':{
        'Coca Codo Sinclaire': [consumos_totales_quito],
        'Sopladora': [consumos_totales_sopladora_quito]
    },
    'Loja':{
        'Sopladora': [consumos_totales_guayaquil],
    
    },
} 
print(consumo_energia2)
ciudad = str(input("ingrese una ciudad: "))
if consumo_energia2.get(ciudad):
    print(consumo_energia2.get(ciudad))     
else:
    print("La ciudad no se encuentra")