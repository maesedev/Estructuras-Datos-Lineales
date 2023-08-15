from random import randint
from linked_list import ListaEnlazada 
from time import sleep

lista1 = ListaEnlazada()
lista2 = ListaEnlazada()
lista4 = ListaEnlazada()


def app():
    llenar_listas()
    printList(lista1,"A")
    printList(lista2,"B")

    lista3 = encontrar_amigos(lista1,lista2)

    print("\nlos elementos en común entre la lista 1 y la lista 3")
    printList(lista3,"C")


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


def encontrar_amigos(lista1, lista2):
    """ Funcion que devuelve una lista de los elementos en comun de las listas  """
    
    # creamos una lista3 que será la que se retorne 
    lista3 = ListaEnlazada()

    def recursive(lista3, nodo):

        # Si el nodo es null devuelve la lista con todos los nodos que ha encontra
        if nodo is None:
            return lista3
        # si tienen el nodo en comun, se agrega a la lista 3
        if lista1.exists(nodo.data):
            lista3.add_at_end(nodo.data)
        # en otro caso revisa el siguiente nodo
        return recursive(lista3, nodo.next)
    return recursive(lista3, lista2.head)
        






app()

