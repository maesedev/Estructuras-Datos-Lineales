from random import randint
def randix_sort(lista):
    digitos = [[] for i in range(0,10)]

    maximo_digitos = len(str(max(lista)))
    for i in range(0,maximo_digitos):  

        print("lista: ",lista)

        for item in lista:
            if len(str(item)) < maximo_digitos:
                print(item)
                item = ("0" * maximo_digitos + item)[-maximo_digitos]
                print(item)
            digitos[ int( str(item)[-(i+1)] ) ].append(item)
        lista = []

        print("Digitos: ",digitos)

        for j, arr_digito in enumerate(digitos):
            for num in arr_digito:
                lista.append(num)
            digitos[ j ] = []

    return lista



arr = [randint(1,99) for x in range(0,5)]
arr_ordenado = randix_sort(arr)

print(arr_ordenado)