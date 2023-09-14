from  parcial.contigua_list import ListaEnlazada  
from estudiante import Estudiante

def app():
    Estudiantes = ListaEnlazada()
    crearEstudiantes(Estudiantes)
    print("Lista inicial")
    imprimir_estudiantes(Estudiantes)

    print("---------------------------------")
    transformar(Estudiantes)
    imprimir_estudiantes(Estudiantes)
    
def crearEstudiantes(lista):
    index = 1
    for i in [1,0,0,1,0,1,1]:
        gen = "M" if i == 0 else "F"
        est = Estudiante(edad=15, nombre="ana",genero=gen,id=index)
        index +=1
        lista.add_at_end(est)

def BorrarEstudiante(lista,indice):
    lista.eliminar(indice)

def transformar(lista):


    ultimo_elemento = lista.get( lista.size()-1)

    def recursiveM(i):
        est = lista.get(i)
        if est is None:
            return 
        if est.genero == "M" and i % 2 == 0:
            for j in range(i , lista.size()):
                if lista.get(j).genero == "F":
                    masc = est
                    fem = lista.get(j)
                    lista.add_between(j,masc)
                    lista.eliminar(i)
                    lista.add_between(i,fem)
                    lista.eliminar(j+1)
                    break
        return recursiveM(i + 1)
            
    
    def recursiveF(i):
        est = lista.get(i)
        if est is None:
            return 
        
        if est.genero == "F" and i % 2==0:
            for j in range(i , lista.size()):
                if lista.get(j).genero == "M":
                    fem = est
                    masc = lista.get(j)
                    lista.add_between(j,fem)
                    lista.eliminar(i)
                    lista.add_between(i,masc)
                    lista.eliminar(j+1)
                    break
                
        return recursiveF(i + 1)
    
         
    if ultimo_elemento.genero == "M":
        
        print("El ultimo es Masculino")
        recursiveM(0)
    else:
        
        print("El ultimo es Femenino")
        recursiveF(0)


def imprimir_estudiantes(lista):
    str = ""
    for i in range(lista.size()):
        est = lista.get(i)
        str += f"{est.genero}{est.id} =>"
        # print("Nombre: ",est.nombre)
        # print("Edad: ",est.edad)
        # print("Genero: ",est.genero)
        # print("Id: ",est.id)
        # print("  ↓ ")
        
    str += "null"
    print(str)






app()

    
