from random import randint 

lista_inicial = [randint(1,20) for x in range(randint(5,30))]
print(lista_inicial)
lista_inicial.sort()
print(lista_inicial)

def recursive(i,stack): 
    """Itera por toda la pila inicial y """
    if len(stack) == 0 or stack[-1] != lista_inicial[i] :
        stack.append(lista_inicial[i])
    if i == 0:
        return stack
    return recursive(i-1, stack)

lista_no_repetida = []
recursive( len(lista_inicial ) - 1, lista_no_repetida ).reverse()
print(lista_no_repetida)
