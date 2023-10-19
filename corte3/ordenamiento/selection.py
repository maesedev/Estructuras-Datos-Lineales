from random import randint

def selection_sort(vector,start=0):
    nb = len(vector)
    for actual in range(start,nb):    
        mas_grande = actual
        for j in range(actual+1,nb) :
            if vector[j] > vector[mas_grande] :
                mas_grande = j
        if min is not actual :
            temp = vector[actual]
            vector[actual] = vector[mas_grande]
            vector[mas_grande] = temp


arr = [randint(1,100) for x in range(1,10)]

selection_sort(arr,3)
print(arr)

selection_sort(arr)

print(arr)
