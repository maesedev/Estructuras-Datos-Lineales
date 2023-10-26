from random import randint

def selection_sort(vector,start=0):
    """Ordenamiento por seleccion"""
    nb = len(vector)
    for actual in range(start,nb):   
        mas_pequeño = actual
        for j in range(actual+1,nb) :
            if vector[j] < vector[mas_pequeño] :
                mas_pequeño = j
        if min is not actual :
            temp = vector[actual]
            vector[actual] = vector[mas_pequeño]
            vector[mas_pequeño] = temp



arr = [randint(1,20) for x in range(1,40)]



selection_sort(arr)
print(arr)

arr.append(0)


contador = 1
for i,item in enumerate(arr):
    num_actual = item
    if i == len(arr) - 1:
        break
    if arr[i + 1] == num_actual:
        contador += 1
    else:
        print(f"El numero {num_actual} se repite {contador} veces")
        num_actual = arr[i + 1]
        contador = 1


    