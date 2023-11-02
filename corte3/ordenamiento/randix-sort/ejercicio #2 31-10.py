from random import randint

def randix_sort_modificado(codigos_list, cantidades_list, precios_list):

    # [ [0] , [1] , [2],..., [9] ]
    # [ [ 1000,  cantidad ,  [precios] ]  ,
    #                   ,...,
    #  [ [1090] ,  cantidad ,  [precios] ]]

    

    digitos = [ [None , 0 , []]  for i in range(0,10)]
    N_elem =  len(codigos_list)
    print("\nlista previa: ",codigos_list)
    print("\nOrdenando...\n")

    for i in range(0, N_elem):
        index = int(str(codigos_list[i]) [2] )

        digitos[ index ][0] = codigos_list[i]
        digitos[ index ][1] += cantidades_list[i]
        digitos[ index ][2].append(precios_list[i])
        
    # Vaciar las listas
    codigos_list = []
    cantidades_list = []
    precios_list = []

    ## volver a llenar las listas
    for item in digitos:
        # En el caso de que no se haya llenado una posicion, no lo agregamos a las listas finales
        if item[0] is None:
            continue
        codigos_list.append( item[0] )
        cantidades_list.append( item[1] )
        precios_list.append( round(sum(item[2]) / len(item[2])    ,2) )
    # retornar las listas ordenadas
    return [codigos_list, cantidades_list, precios_list]


codigos     = []
cantidades  = []
precios     = []

N = randint(6, 15)

# LLENAR LAS LISTAS CON DATOS ALEATORIOS #
for i in range(0,N):
    codigos.append( f"10{ randint(0,9) }0" )
    cantidades.append( randint(0,59) )
    precios.append( randint(1, 30) * 10 )


for i in range(0,N):
    print(f"Codigo: {codigos[i]} \tCantidad: {cantidades[i]} \tPrecio: {precios[i]}")


[
codigos_ordenado,
cantidades_ordenado,
precios_ordenado
]  =                    randix_sort_modificado(codigos,cantidades, precios )


for i in range(0,len(codigos_ordenado)):
    print(f"Codigo: {codigos_ordenado[i]} \tCantidad: {cantidades_ordenado[i]} \tPrecio: {precios_ordenado[i]}")
