
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

        # Iteramos desde la cabeza, hasta encontrar el ultimo elemento, que NODO.next seria NULL 
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

        self.numero_elementos += 1
    
    # def delete_node(self, key):
    #     """ Método para eleminar nodos """
    #     #Iniciamos al principio de la lista
    #     curr = self.head
    #     prev = None

    #     while curr and curr.data != key:
    #         #busca en cada nodo si el KEY es igual al nodo actual
    #         prev = curr
    #         #Pasamos al siguiente nodo para reiniciar la iteracion
    #         curr = curr.next


    #     # Si el elemento que queremos eliminar es el primero entonces hacemos que la cabeza sea el siguiente elemento
    #     if prev is None:
    #         self.head = curr.next
    #         prev.next = curr.next
    #         curr.next = None

    #     self.numero_elementos -= 1

    def get_last_node(self):
        """Método para obtener el ultimo nodo"""
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    def exists(self,data):
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
        Node = self.head
        print("\nlista ",nombre)
        list_elements_string =""
        while Node is not None:
            list_elements_string += str(Node.data) + " => "
            Node = Node.next
        list_elements_string += " null"    
        print(f"{list_elements_string}\n")

    def get(self,i):
        if i > self.numero_elementos: 
            return "Error: List out of range"
        n = 0
        node = self.head
        def recursive (n,node):
            if n == i:
                return node.data
            return recursive( n+1 , node.next)
        return recursive(n, node)
    

list = ListaEnlazada()

list.add_at_end(20)
list.add_at_end(30)
list.add_at_end(40)
list.add_at_end(50)
list.add_at_end(60)

list.print_list(nombre="A")
print(list.get(2))