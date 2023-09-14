lista = [0,1,2,3,4,5,6]
lista1 = [0,1,2,3,4,5,6]

def llenar(size):
    data=0
    if(size < 0):
        return
    else :
        data = lista[size]
        llenar(size-1)
    llenarR(data,size)

def llenarR(data, size):
    lista1[size] = data;

llenar(5)
print(lista)
print(lista1)