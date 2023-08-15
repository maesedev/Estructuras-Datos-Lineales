
class Node:
    """Inicializacion del nodo"""
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class ListaEnlazada:
    """Lista enlazada"""
    def __init__(self,numero_elementos):
        self.head = None
        self.numero_elementos = numero_elementos
    
    def add_at_front(self, data):
        """Método para agregar elementos en el frente de la linked list"""
        self.head = Node(data=data, next=self.head)  

    def is_empty(self):
        """Método para verificar si la estructura de datos esta vacia"""
        return self.head is None

    
    def add_at_end(self, data):
        """Método para agregar elementos al final de la linked list"""
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)
    
    def delete_node(self, key):
        """ Método para eleminar nodos """
        curr = self.head
        prev = None

        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def get_last_node(self):
        """Método para obtener el ultimo nodo"""
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    def print_list( self ):
        """Método para imprimir la lista de nodos"""
        Node = self.head
        while Node is not None:
            print(Node.data, end =" => ")
            Node = Node.next




