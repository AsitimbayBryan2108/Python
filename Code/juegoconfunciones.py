import random 
op = -1
empates = 0
ganados = 0
perdidos = 0

def menu():
    print("<1> jugar")
    print("<2> resultados")
    print("<3> salir")

def menu2 ():
    print("<1> piedra")
    print("<2> papel")
    print("<3> tijera")
    print("<4> menu principal")

def menu3 ():
    print("empates: ",empates)
    print("victorias ",ganados)
    print("derrotas: ",perdidos)
    print("<3> salir")
    print("<4> menu principal")

def quit ():
    print("programa finalizado")
    quit()

def quit2 ():
    print("programa finalizado")
    quit()

if op == 4:
    menu()
while op != 0:
    menu()
    op = int(input("ingrese una opcion: "))
    if op == 1:
        while op != 4:
            menu2()
            op = int(input("ingrese eleccion: "))
            num = random.randint(1, 3)
            if op== num:
                    print ("Empate")
                    empates+=1
            elif op==1:
                if num==2:
                        print ("elijo piedra",op,"vs","papel",num,"pierdo")
                        perdidos+=1
                elif num ==3:
                        print ("elijo piedra",op,"vs","tijera",num,"gano")
                        ganados+=1
            elif op==2:
                if num==1:
                        print ("elijo papel",op,"vs","piedra",num,"gano")
                        ganados+=1
                elif num==3:
                        print ("elijo papel",op,"vs","tijera",num,"pierdo")
                        perdidos+=1
            elif op==3:
                if num==1:
                        print ("elijo tijera",op,"vs","piedra",num,"pierdo")
                        perdidos+=1
                elif num==2:
                        print ("elijo tijera",op,"vs","papel",num,"gano")
                        ganados+=1
            elif op >= 5:
                print("ingrese una opcion correcta")
    elif op == 2:
        menu3()
        regresar = int(input("ingresar eleccion: "))
        if regresar == 3:
            quit ()
    elif op == 3:
        quit2()
    else:
        print("ingrese una opcion correcta")