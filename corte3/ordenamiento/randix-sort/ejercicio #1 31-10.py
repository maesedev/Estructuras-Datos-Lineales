from random import randint
def randix_sort(lista):
    # creamos una lista de 9 listas
    digitos = [[] for i in range(0,10)]

    # Es para saber si en la lista hay numeros de diferentes cantidades de digitos 
    maximo_digitos = len(str(max(lista)))
    for i in range(0,maximo_digitos):  
        
        print(f"lista, iteracion {i+1}: \t",lista)


        for item in lista:
            if len(str(item)) < maximo_digitos:
                # si el numero tiene menos digitos que el de maximos digitos, le antepone 0s (0008, 0015, 0128,...) 
                temp = str(f"{'0' * maximo_digitos}{str(item)}")[-maximo_digitos:]
                digitos[ int( str(temp)[-(i+1)] ) ].append( int(temp) )
            else:
                # sino solamente lo agrega a la lista digitos
                digitos[ int( str(item)[-(i+1)] ) ].append(item)
        # vaciamos la lista
        lista = []
        print("Digitos: ",digitos,"\n")

        for j, arr_digito in enumerate(digitos):
            for num in arr_digito:
                lista.append(num)
            digitos[ j ] = []

    return lista



arr = [randint(100,999) for x in range(0,5)]
arr_ordenado = randix_sort(arr)

print(arr_ordenado)