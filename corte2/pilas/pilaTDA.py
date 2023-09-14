class NodoPila:
    """ Nodo en el que se guarda los elementos de la pila """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaLista:
    """ Una pila """
    def __init__(self):
        self.cima = None
        self.cantidad_elementos = 0
    
    def is_empty(self):
        """ verificar si la pila está vacía """
        return self.cima == None
    
    def push(self,dato):
        """ Inserta un dato en la cima de la pila """
        nuevo = NodoPila(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo
        self.cantidad_elementos += 1
    
    def InsertarIndex(self,index, data):
        """ Inserta un dato en un indice dado """
        return 

    def remove(self):
        """ Quita el dato de la cima de la pila """
        if self.is_empty():
            raise ValueError("Error, no se puede eliminar elementos que no existen")
        self.cantidad_elementos -= 1
        
        aux = self.cima.dato
        self.cima = self.cima.siguiente
        return aux

    def get_cima(self):
        """ Obtiene el dato de la cima de la pila, sin desapilarlo """
        if self.is_empty(): 
            raise ValueError("Error: Pila vacia, la pila no tiene cima aun")
        return self.cima.dato
    
    def clean(self):
        """ Limpia la pila """
        self.cima = None
        self.cantidad_elementos = 0

    def size(self):
        """ Cantidad de elementos en la pila """
        return self.cantidad_elementos
    
    def print(self):
        """ imprime la pila con la forma
         pila
        |  a  | 
        |  a  |
        |  a  |
        |  a  |
        |__a__|
        """

        if self.is_empty():
            print("\n   pila")
            print("|___empty___|")
            return

        pila_copy = PilaLista()

        print("\n    Pila")
        max_range = self.size()

        for i in range(max_range):
            pila_copy.push(self.get_cima())
            if i == max_range - 1:
                print("|___",self.get_cima(),"___|")
            else:
                print("|   ",self.get_cima(),"   |")
            self.remove()

        for i in range(pila_copy.size()):
            self.push(pila_copy.get_cima())
            pila_copy.remove()
        del pila_copy

        
    def toString(self):
        """ imprime la pila con la forma
        [a,b,c,d]

        """
        pila_copy = PilaLista()
        max_range = self.size()

        str = "["

        for i in range(max_range):
            pila_copy.push(self.get_cima())
            str += f"{self.get_cima()}"+ ("" if i == max_range - 1 else "," )
            self.remove()

        for i in range(pila_copy.size()):
            self.push(pila_copy.get_cima())
            pila_copy.remove()
        
        del pila_copy

        str +="]"
        print(str)


