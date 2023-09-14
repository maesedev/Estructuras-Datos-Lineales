from random import randint 

lista_inicial = [randint(1,20) for x in range(randint(5,30))]
lista_inicial.sort()
print(lista_inicial)

divisor = int(input("ingrese el divisor X: "))
# divisor = 2
print(divisor)

def recursive(i,stack): 
    if lista_inicial[i] % divisor != 0:
        stack.append(lista_inicial[i])
    if i == 0:
        return stack
    return recursive(i-1, stack)

lista_sin_divisores = []

recursive(len(lista_inicial) - 1, lista_sin_divisores).reverse()

print(lista_sin_divisores)
