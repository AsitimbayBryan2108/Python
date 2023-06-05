dia = 30
mes = 11

anho = 2020
print(dia, mes, anho)

ultimo_dia = 30

if mes == 2:
    if anho%4 == 0 and anho%100 != 0 or anho%400 == 0:
        ultimo_dia = 29
    else:
        ultimo_dia = 28
elif mes in (1,3,5,7,8,10,12):
    ultimo_dia = 31


if dia == ultimo_dia:
    dia = 1
    if mes == 12:
        mes = 1
        anho += 1
    else:
        mes += 1
else:
    dia += 1

print(dia, mes, anho)