from random import randint
from linked_list import ListaEnlazada

lista = []
pila = []

for i in range(randint(2,15)):
    lista.append( "M" if (randint(0,1) == 1) else "F"  )

print(lista)


ultimo = lista[len(lista) - 1]  ## obtiene "M" o "F"
cantidad_masculinos = lista.count("M")


for i in range(cantidad_masculinos):
    pila.append("M")
    lista.remove("M")

print("cantidad_masculinos: ",cantidad_masculinos)


# si el ultimo es masculino el primero debe de ser femenino y viceversa
lenght = len(pila) + len(lista)  #20
print("lenght: ",lenght)

i=0
j=0

if ultimo =="M":
    for i in range(0,lenght,2):
        print(i)
else:
    for i in range(2,lenght,2):
        print(i)
