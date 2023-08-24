from modules.linked_list import ListaEnlazada 
from modules.producto import Producto 
from random import randint

def app():
    """Función principal"""
    Productos = crear_productos()
    mostrar_productos(Productos)
    con_codigo_par(Productos)
    promedio(Productos)

def crear_productos():
    """Crear una la lista encadenada que contenga instancias de la clase Producto, cada producto al
    crearse tiene los siguientes datos: código, nombre, cantidad y precio (los datos cantidad y
    precio se generan aleatoriamente), el código del producto será un numero consecutivo que
    debe iniciar en 1000, el nombre del producto será básico (producto1, producto 2, producto3,
    productoN). El número de productos en la lista ser un número aleatorio entre 10 y 30"""
    lista = ListaEnlazada()
    id_producto = 1
    for i in range( randint(10,30) ):
        price = randint(1000,500000)
        cantidad = randint(1,1000)

        producto = Producto(
            codigo=1000 + i,
            cantidad=cantidad,
            nombre=f"producto {id_producto}",
            precio=price
            )
        id_producto += 1
        
        lista.add_at_end(producto)

    return lista

    
def mostrar_productos(lista):
    """Muestra todos los productos, y un null al final"""
    for i in range(lista.size()):
        product = lista.get(i)
        print(f"Codigo: {product.codigo}")
        print(f"Nombre: {product.nombre}")
        print(f"Precio: ${product.precio}")
        print(f"Cantidad: {product.cantidad}")
        print("\t|")
        print("\t↓")
    print("\tNull")

def con_codigo_par(lista):
    """Calcular el precio total de los productos cuyo código sea un número par y mostrar los
datos de cada producto.
"""
    print("\n--- Productos con codigo par ---")
    for i in range(lista.size()):
        product = lista.get(i)
        if product.codigo % 2 == 0 :
            print(f"Codigo: {product.codigo}")
            print(f"Nombre: {product.nombre}")
            print(f"Precio: ${product.precio}")
            print(f"Cantidad: {product.cantidad}")
            print("\t|")
            print("\t↓")
    print("\tNull")

def promedio(lista):
    """Mostrar por consola el precio medio de todos los productos y mostrar la cantidad de
productos en la lista. Implementar una función (método) recursivo."""
    def recursive(suma,cantidad, i):
        """"""
        product = lista.get(i)
        if product is None:
            return [suma, cantidad]
        return recursive(suma + product.precio, cantidad + product.cantidad,  i + 1)
    i = 0
    [suma_precios,cant_productos] = recursive(0,0,i)

    print(f"\nLa cantidad total de productos es: {cant_productos}")
    prom = round(suma_precios / lista.size())
    print(f"El precio medio de todos los  productos es: ${prom}")



app()
