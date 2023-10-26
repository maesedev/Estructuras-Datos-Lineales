from random import randint

def ordenar_pedidos(producto,cantidad,precio,start=0):
    """Ordenamiento por seleccion"""
    nb = len(producto)

    for actual in range(start,nb):   
        mas_pequeño = actual
        for j in range(actual+1,nb) :
            if producto[j] < producto[mas_pequeño] :
                mas_pequeño = j
        if min is not actual :
            producto_temp = producto[actual]
            cantidad_temp = cantidad[actual]
            precio_temp = precio[actual]

            producto[actual] = producto[mas_pequeño]
            cantidad[actual] = cantidad[mas_pequeño]
            precio[actual] = precio[mas_pequeño]

            producto[mas_pequeño] = producto_temp
            cantidad[mas_pequeño] = cantidad_temp
            precio[mas_pequeño] = precio_temp
            

N = randint(20,50)
producto = [1000 + (randint(1,6) * 10) for x in range(1,N)]
cantidad = [randint(1,20) for _ in range(1,N)]
precio = [randint(1,50) for _ in range(1,N)]


print(producto)
print(cantidad)
print(precio)

ordenar_pedidos(producto,cantidad,precio)

print(" -- Ordenado --")




def recursive(i, producto, cantidad, precio):
    if i is len(producto):
        return
    if producto[i + j] == num_actual:
        cantidad[i] += cantidad[i+j]
        precio[i] += precio[i+j]
        
        producto.remove(i+j)
        cantidad.remove(i+j)
        precio.remove(i+j)

    


contador = 1
for i,item in enumerate(producto):
    num_actual = item
    if i == len(producto) - 1:
        break
    j=1
    while producto[i + j] == num_actual:
        cantidad[i] += cantidad[i+j]
        precio[i] += precio[i+j]
        
        producto.remove(i+j)
        cantidad.remove(i+j)
        precio.remove(i+j)
        j += 1
    
    else:
        print(f"El numero {num_actual} se repite {contador} veces")
        num_actual = producto[i + 1]
        contador = 1

        
print(producto)
print(cantidad)
print(precio)


