
lista=[1,2,3,4,5,6,8]
n=2

#for i in range(len(lista)):
# print(lista[i])

#print()
control=False
posicion=0

for val in lista:
    if val == n:
        control=True
        break
    posicion+=1

if control:
    print("Se encontro el numero", n,"en la posicion",posicion)
else:
    print("No se encontro el numero",n)