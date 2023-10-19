from random import randint

""" Escriba una función que reciba una lista de N elementos y permita hallar la
frecuencia de repetición de cada elemento. """


def app():

    n = input("Ingrese la cantidad máxima (n) de elementos para la lista: ")
    try:
        n = int(n)
    except ValueError:
        print(f"Lo siento \"{n}\"  no es un numero, usaremos entonces n = 10")
        n = 10

    lista_inicial = [randint(1,20) for x in range(n)]
    lista_inicial.sort()
    

    def remove_repetidos(i,stack1,stack):
        if i == len(stack1):
            return stack
        if len(stack) == 0  or stack[-1] != stack1[i]:
            stack.append(stack1[i])
        return remove_repetidos(i+1 , stack1,stack)

    unique_stack = remove_repetidos( 0 , lista_inicial , [] )

    print(lista_inicial) 

    for i in range(len(unique_stack)):
        reps = contar_repeticiones(unique_stack[i] , lista_inicial )
        print(f" {unique_stack[i]} --> {reps} repeticiones")

def contar_repeticiones(n,stack):
    """ Cuenta cuantas veces se repite un numero en una pila"""
    
    def recursive(i,reps):
        if stack[i] == n: 
            reps +=1
        if i == 0: return reps 
        return recursive(i-1, reps)
    
    return recursive(len(stack) - 1,0)


app()