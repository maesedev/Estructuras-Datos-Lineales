from random import randint
from modules.linked_list import ListaEnlazada
from time import sleep

lista1 = ListaEnlazada()
lista2 = ListaEnlazada()


def app():

    print("\n\t----- Creación de listas -----\n")
    llenar_listas()
    sleep(3)
    print("\n")
    printList(lista1,"1")
    sleep(1)
    printList(lista2,"2")
    sleep(1)

    lista3 = encontrar_enemigos(lista1,lista2)

    
    print("\nlos elementos que estan en la lista 1 y no en la lista 2 son: ")
    printList(lista3,"3")
    sleep(1)

    lista4 = añadir_pares_impares(lista1,lista2)

    
    sleep(1)
    print("\nlos elementos pares de la lista 1 y los impares en la lista 2 son: ")
    printList(lista4,"4")


def printList(list,name):
    list.print_list(name)

def llenar_listas():
    """LLenar las listas con datos aleatorios segun corresponda"""

    cant_elem_l1 = randint(10,30)
    print(f"Se crearán {cant_elem_l1} de nodos para la lista 1")

    while lista1.numero_elementos < cant_elem_l1:
        lista1.add_at_end(randint(50,550))

    cant_elem_l2 = randint(1,115)
    print(f"Se crearán {cant_elem_l2} de nodos para la lista 2")

    while lista2.numero_elementos < cant_elem_l2:
        lista2.add_at_end(randint(50,550))


def encontrar_enemigos(lista1, lista2):
    """ Crear una tercera lista que contenga los elementos que están en la lista 1 y no están en 
        la lista 2. Se debe implementar una función (método) recursivo."""
    
    # creamos una lista3 que será la que se retorne 
    lista3 = ListaEnlazada()
    
    def recursive(lista3, index):

        # Si llega al ultmo elemento devuelve la lista con todos los nodos que ha encontrado
        if index == lista1.numero_elementos:
            return lista3
        
        # si tienen el dato esta en la lista 1 y no en la lista 2, se agrega a la lista 3
        dato_actual = lista1.get(index)
        if not lista2.exist(dato_actual):
            lista3.add_at_end(dato_actual)

        # en otro caso revisa el siguiente dato de la lista 1
        return recursive(lista3, index + 1)
        
    return recursive(lista3, 0)
        

def añadir_pares_impares(lista1, lista2):
    """Crear una cuarta lista que contenga los elementos de la lista 1 que son pares y los 
        elementos de la lista 2 que son impares."""

    lista4 = ListaEnlazada()
    maxindex = lista1.numero_elementos if ( lista1.numero_elementos > lista2.numero_elementos) else lista2.numero_elementos
    
    def recursive(lista, i):
        # Si llega al ultmo elemento devuelve la lista con todos los nodos que ha encontrado
        if i == maxindex:
            return lista

        if i <= lista1.numero_elementos:
            dato_lista1 = lista1.get(i)
            if dato_lista1 % 2 == 0:
                lista.add_at_end(dato_lista1)


        
        if i <= lista2.numero_elementos:
            dato_lista2 = lista2.get(i)
            if dato_lista2 % 2 == 1:
                lista.add_at_end(dato_lista2)
        return recursive(lista, i + 1)
        

    return recursive (lista4, 0)






app()

