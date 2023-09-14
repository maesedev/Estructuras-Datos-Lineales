stack = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

def intercambiar(stack):
    """Intercambia el primero y ultimo elemento de la pila"""
    print(stack)
    ultimo = stack.pop()

    print("ultimo: ", ultimo)
    primero = stack[0]
    print("primero: ", primero)


    def recursive(i):
        if i == 1:
            stack.pop()
            stack.append(ultimo)

            return primero
        a = stack.pop()
        recursive(i-1)
        return stack.append(a)
    
    recursive(len(stack))
    stack.append(primero)
    print(stack)



intercambiar(stack)
