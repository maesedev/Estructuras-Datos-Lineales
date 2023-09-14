class NodoPila:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None

class PilaLista:
    def __init__(self):
        self.cima = None
    
    def pila_vacia(self):
        return self.cima == None
    
    def insertar(self,elemento):
        nuevo = NodoPila(elemento)
        nuevo.siguiente = self.cima
        self.cima = nuevo
    def quitar(self):
        if self.pila_vacia():
            raise Exception("Error, no se puede eliminar elementos que no existen")
        
        aux = self.cima.elemento
        self.cima = self.cima.siguiente
        return aux

    def get_cima_pila(self):
        if self.pila_vacia(): 
            raise Exception("Error: Pila vacia, la pila no tiene cima aun")
        return self.cima.elemento
    
    def limpiar_pila(self):
        while self.pila_vacia():
            t = self.cima
            self.cima = self.cima.siguiente
            t.siguiente = None
        