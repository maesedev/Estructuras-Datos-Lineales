class Robot:

    def __init__(self,ID,tipo, bateria):
        self.ID = ID
        self.tipo = tipo
        self.bateria = bateria
    
    def Imprimir(self,nombre):
        print ("Hola soy "+ nombre +" con id "+ self.ID )

    def reducirBateria(self, cantidad):
        self.bateria -=  cantidad
        print(f"Redujimos {cantidad}% de bateria")


    
r1 = Robot(ID="87ASDF6H",tipo="Mecanico",bateria=50)

r1.Imprimir("carlos")
r1.reducirBateria(50)