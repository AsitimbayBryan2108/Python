op = -1
num1 = 0
num2 = 0

while op != 0:


    print('<1> sumar')
    print('<2> restar')
    print('<3> multiplicar')
    print('<4> dividir')
    print('<5> salir')

    op = int(input('Ingrese opcion:'))

    if op != 0 :
        num1 = int(input('Ingresar numero 1:'))
        num2 = int(input('Ingresar numero 2:'))
    
    if op ==1 :
        print('suma:',num1+num2)
    elif op ==2 :
        print('resta:',num1-num2)
    elif op ==3 :
        print('multiplicacion:', num1*num2)
    elif op == 4 :
        print('division:',num1/num2)
    else :
        print ('no existe la opcion.')