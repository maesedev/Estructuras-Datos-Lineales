from random import randint

lista_inicial = [randint(1,20) for x in range(randint(5,30))]
lista_inicial.sort()
while True:

    print("Lista inicial: ",lista_inicial)

    print("Ingrese \"EXIT\", para salir")
    X = input("ingrese el numero a agregar a la lista: ").upper()
    if X.find("EXIT") != -1:
        print("Good Bye")
        break
    X = int(X)

    def recursive(i,stack):
        if i == len(stack) - 1:
            return
        if stack[i] < X:
            return recursive ( i + 1,stack)
        else:
            print(f"Elemento {X} agregado en el indice {i}\n\n")
            stack.insert(i,X)
            return
    recursive(0,lista_inicial)