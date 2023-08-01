
def sum_array(array,i):
    if i == 0:
        return array[0]
    return int(array[i]) + int(sum_array(array , i - 1))

Array = [5,10,25,65,32,45]

print(sum_array(Array , 5 ))