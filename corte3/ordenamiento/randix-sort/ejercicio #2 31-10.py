from random import randint

def randix_sort_modificado(lista):
    digitos = [[] for i in range(0,10)]

    maximo_digitos = len(str(max(lista)))
    for i in range(0,maximo_digitos):  

        print("lista: ",lista)

        for item in lista:
            if len(str(item)) < maximo_digitos:
                temp = str(f"{'0' * maximo_digitos}{str(item)}")[-maximo_digitos:]
                digitos[ int( str(temp)[-(i+1)] ) ].append( int(temp) )
            else:
                digitos[ int( str(item)[-(i+1)] ) ].append(item)
        lista = []
        print("Digitos: ",digitos)

        for j, arr_digito in enumerate(digitos):
            for num in arr_digito:
                lista.append(num)
            digitos[ j ] = []

    return lista


codigos     = []
cantidades  = []
precios     = []

N = randint(6, 15)

# LLENAR LAS LISTAS CON DATOS ALEATORIOS #
for i in range(0,N):
    codigos.append( f"10{ randint(0,9) }0" )
    cantidades.append( randint(0,59) )
    precios.append( randint(1, 30) * 10 )


print(codigos)
print(cantidades)
print(precios)



