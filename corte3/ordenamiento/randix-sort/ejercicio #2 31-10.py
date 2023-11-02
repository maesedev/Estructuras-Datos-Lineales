from random import randint
from statistics import mean


class producto():
    def __init__(self, codigo, cantidad, precios):
        self.codigo = codigo
        self.cantidad = cantidad
        self.precios = precios


def randix_sort_modificado(productos):
    """ ordena los productos  """
    
    
    digitos = [ producto(codigo=None, cantidad=0 , precios = [])  for i in range(0,10)]

    N_elem =  len(productos)

    str="["
    for i in productos:
        str += f"{i.codigo}, "
    print(str+"]")

    print("\nOrdenando...\n")

    for i in range(0, N_elem):

        index = int((""+productos[i].codigo)[2])

        digitos[ index ].codigo = productos[i].codigo
        digitos[ index ].cantidad += productos[i].cantidad
        digitos[ index ].precios.append(productos[i].precios)

    productos = []

    ## volver a llenar las listas
    for item in digitos:
        
        # En el caso de que no se haya llenado una posicion, no lo agregamos a las listas finales
        if item.codigo is None:
            continue
        productos.append(producto(codigo=None, cantidad=0 , precios = []))
        productos[-1].codigo =  item.codigo 
        productos[-1].cantidad =  item.cantidad 
        
        productos[-1].precios = round( mean(item.precios) )

    # retornar los productos
    return productos



productos  = []

N = randint(6, 20)

# LLENAR CON DATOS ALEATORIOS #
for i in range(0,N):
    productos.append( producto(codigo=f"10{ randint(0,9) }0", cantidad=randint(0,59) , precios = randint(1, 30) * 10) )

for product in productos:
    print(f"Codigo: {product.codigo} \tCantidad: {product.cantidad} \tPrecio: {product.precios}")

productos = randix_sort_modificado(productos)

for product in productos:
    print(f"Codigo: {product.codigo} \tCantidad: {product.cantidad} \tPrecio: {product.precios}")

