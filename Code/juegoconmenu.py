
#jugar
#elegir una opcion
#resultados
#gane,pierda,empata
#salir
import random

op = -1
juego = -1 
empates=0
ganados=0
perdidos=0

def menu ():
    print("<1> jugar")
    print("<2> resultados")
    print("<3> salir")    
while op != 0:
        menu ()
        op = int(input("ingrese una opcion: "))
        if op == 1:
            while juego != 4:
                print("<1> piedra")
                print("<2> papel")
                print("<3> tijera")
                print('<4> regresar')
                juego = int(input("ingrese su eleccion: "))
                if juego == 4:
                    menu()
                num = random.randint(1,3)
                if juego== num:
                    print ("Empate")
                    empates+=1
                elif juego==1:
                    if num==2:
                        print ("elijo piedra",juego,"vs","papel",num,"pierdo")
                        perdidos+=1
                    elif num ==3:
                        print ("elijo piedra",juego,"vs","tijera",num,"gano")
                    ganados+=1
                elif juego==2:
                    if num==1:
                        print ("elijo papel",juego,"vs","piedra",num,"gano")
                        ganados+=1
                    elif num==3:
                        print ("elijo papel",juego,"vs","tijera",num,"pierdo")
                    perdidos+=1
                elif juego==3:
                    if num==1:
                        print ("elijo tijera",juego,"vs","piedra",num,"pierdo")
                        perdidos+=1
                    elif num==2:
                        print ("elijo tijera",juego,"vs","papel",num,"gano")
                    ganados+=1
                else:
                    print("ingrese una opcion correcta")
        elif op == 2:
            print("ganados: ",ganados)
            print("perdidos: ", perdidos)
            print("empatados: ",empates)
        elif op == 3:
            quit()
        else:
            print("ingrese una opcion correcta")