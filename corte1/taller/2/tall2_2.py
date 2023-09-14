from parcial.contigua_list import ListaEnlazada


""""En caso de que la suma de los datos que se encuentran contenidas 
en los elementos que ocupan posiciones impares, sea igual a la suma de los datos que se encuentran contenidas 
en los elementos que ocupan posiciones pares, se deberá borrar de la lista todos los elementos que ocupan 
posiciones pares"""
def app():
    lista = ListaEnlazada()
    lista.add_at_end(1)
    lista.add_at_end(2)
    lista.add_at_end(3)
    lista.add_at_end(4)
    lista.add_at_end(5)

    lista.print_list("A")
    print("\n")
    if sumar_pares(lista) ==   sumar_impares(lista):
        borrar_pares(lista)
    else: 
        borrar_impares(lista)
    
    lista.print_list("A")
    
def borrar_impares(lista):
    par_impar = True
    
    for i in range(lista.size()):

        if par_impar and i % 2 == 1:
            lista.eliminar(i)
            par_impar = False
        else:
            par_impar = True


def borrar_pares(lista):
    return 


def sumar_pares(lista):
    """suma los pares de la lista"""
    def recursive(i,suma):
        if i == lista.size():
            return suma
        if i % 2 == 0:
            suma += lista.get(i)
        return recursive(i+1,suma)
    
    return recursive( 0 , 0)

def sumar_impares(lista):
    """suma los impares de la lista"""
    def recursive(i,suma):
        if i == lista.size():
            return suma
        if i % 2 == 1:
            suma += lista.get(i)
        return recursive(i+1,suma)
    
    return recursive( 0 , 0)



app()