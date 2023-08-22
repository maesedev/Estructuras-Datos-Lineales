
class Node:
    """Inicializacion del nodo"""
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


# Creamos la clase linked_list
class ListaEnlazada:
    """Lista enlazada"""
    def __init__(self):
        self.head = None
        self.numero_elementos = 0
    
    def add_at_start(self, data):
        """Método para agregar elementos en el frente de la linked list"""
        self.head = Node(data=data, next=self.head)  
        self.numero_elementos += 1

    def is_empty(self):
        """Método para verificar si la estructura de datos esta vacia"""
        return self.head is None

    
    def add_at_end(self, data):
        """Método para agregar elementos al final de la linked list"""
        # Si no hay elementos entonces el ultimo es el primero, ya que seria un solo elemento
        if self.is_empty():
            self.head = Node(data=data)
            return
        # Iniciamos desde el principio de la lista
        curr = self.head
        # Iteramos desde la cabeza, hasta encontrar el ultimo elemento, que NODO.next seria None 
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

        self.numero_elementos += 1

    def get_last_node(self):
        """Método para obtener el ultimo nodo"""
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.data

    def exist(self,data):
        """Método para saber si existe un nodo con cierto valor"""
        # Si no hay elementos entonces no existe porque no hay elementos
        if self.is_empty():
            return False
        
        # Iniciamos desde el principio de la lista
        curr = self.head

        # Iteramos desde la cabeza, hasta encontrar el ultimo elemento, que NODO.next seria NULL 
        while curr is not None and curr.data != data :
            if curr.data == data:
                return True
            
            curr = curr.next
            if curr.next is None:
                return False
        return True



    def print_list( self, nombre ):
        """Método para imprimir la lista de nodos"""

        if self.is_empty():
            print("la lista esta vacia")
            return 
        
        # Nos posicionamos desde la cabeza
        Node = self.head
        print("lista ",nombre)

        list_elements_string =""

        while Node is not None:
            list_elements_string += str(Node.data) + " => "
            Node = Node.next

        list_elements_string += "null"    
        print(f"{list_elements_string}\n")

    def get(self,i):
        """Funcion recursiva para encontrar un elemento por el indice de la lista"""
        if i > self.numero_elementos: 
            return "Error: List out of range"
        
        n = 0
        # nos posicionamos desde la cabeza para iterar a travez de la lista
        node = self.head

        def recursive (n,node):
            if n == i:
                return node.data
            return recursive( n+1 , node.next)
        
        return recursive(n, node)
    
    def add_between(self, index, data):
        """Función que agrega un elemento entre nodos"""

        if index > self.numero_elementos: 
            return "Error: List out of range"

        # Si queremos agregar entre el primer y segundo nodo, osea en el indice 0
        if index == 0:
            self.add_at_start(data)
            return
        
        # Iniciamos desde el principio de la lista
        curr = self.head

        # Posiciononarse en el nodo que necesito (indice - 1)
        for _ in range(index - 1):
            curr = curr.next
        
        new_node = Node(data=data, next=curr.next)
        curr.next = new_node
        self.numero_elementos += 1
    
    def edit(self,index, data):
        if self.is_empty():
            return False
        curr = self.head

        if self.size()-1 < index:
            print("Error")
            return False

        for _ in range(index - 1):
            curr = curr.next
        curr.data = data
        return True

    def size(self):
        return self.numero_elementos

    # def delete_element(self, index):
    #     """Función que elimina el elemento en el índice dado de la lista"""

    #     if index == 0:

    #     return 

