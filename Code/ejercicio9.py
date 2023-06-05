#Dada la fecha de hoy
#Calcular la fecha del dia siguiente
#Suponer que el año no es bisiesto

dia=int(input("Ingrese un dia: "))
mes=int(input("Ingrese un mes: "))
año=int(input("Ingrese un año: "))
if mes<=0 or mes>12 or dia<=0 or dia>31 or año<0: 
    print("fecha ingresada no valida")
elif mes in [1, 3, 5, 7, 8, 10, 12]: 
    if dia==31 and mes==12: 
        año=año+1 
        mes=1
        dia=1
    elif dia==31 and mes!=12:
        mes=mes+1  
        dia=1    
    else:
        dia=dia+1
    print("el dia siguiente es:",(dia,mes,año))
elif mes in [4, 6, 9, 11] and dia<=30: 
    if dia==30: 
        mes=mes+1 
        dia=1
    else:
        dia=dia+1
    print("el dia siguiente es:",(dia,mes,año))
elif mes==2 and dia<=28: 
    if dia==28:
        mes=mes+1 
        dia=1
    else: 
        dia=dia+1 
    print("el dia siguiente es:",(dia,mes,año))
else:
    print("Fecha ingresada no valida")