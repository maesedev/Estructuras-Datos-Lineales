
from collections import deque
from random import randint
import random
from time import sleep

# $ pip3 install yaspin
from yaspin import yaspin

# $ pip3 install InquirerPy
from InquirerPy import inquirer

class auto:
    def __init__(self,placa):
        self.placa = placa

HORA_ACTUAL = 0
PRECIO_MINUTO = 252
MAX_SIZE = 10
PARQUING_QUEUE = deque(maxlen=MAX_SIZE)
PLACAS = []
PLACAS_DENTRO = []

def generar_PLACAS(n):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for _ in range(n):
        # Generar letras aleatorias (HFG)
        letras_aleatorias = ''.join(random.choice(letras) for _ in range(3))
        
        # Generar números aleatorios (123)
        numeros_aleatorios = ''.join(random.choice('0123456789') for _ in range(3))
        
        # Crear la placa completa (HFG 123)
        placa = f"{letras_aleatorias} {numeros_aleatorios}"
        PLACAS.append(placa)
    return PLACAS



def printQueue():
    copyQ = PARQUING_QUEUE.copy()
    print("\t Parquing List")
    for i in range(len( copyQ )):
        element = copyQ.pop()
        print(i+1,element[0].placa, f" tiempo: {element[2]} minutos \tmovido { element[3]} veces")


def ingresar_auto(placa,tiempo_estadia):
    print("INGRESA AUTO")
    print(f"Placa: {placa}")
    if(tiempo_estadia > 30): return print("Error: El tiempo debe ser menor a media hora \nAuto no ingresado")
    if(len(PARQUING_QUEUE) == MAX_SIZE):return  print("Carril lleno, auto no ingresado")
    ## [   0 ,         1      ,                 2        ,             3       ]
    ## [auto, hora del ingreso, tiempo de estadia ya pago, cant veces movido]
    PARQUING_QUEUE.appendleft( [auto(placa), HORA_ACTUAL, tiempo_estadia, 0 ] )
    print("Auto ingresado correctamente")

 
def retirar_auto(placa):

    if len(PARQUING_QUEUE) == 0: 
        return print("No hay autos aun estacionados"), False
    
    # encontrar el auto, ver si está en la primera o en otra posición
    # ver si su tiempo esta bien sino poner multa
    multa = False
    element = PARQUING_QUEUE.popleft()

    if element[0].placa == placa:
        multa = verificar_tiempo(element[1], HORA_ACTUAL)
        if not multa:
            cobrar( HORA_ACTUAL - element[1])
            
        print("\nSE RETIRA AUTO")
        print(f"Placa: {placa}")
        print("Auto retirado correctamente\n")
        return element,True
    
    element[3] += 1
    PARQUING_QUEUE.appendleft(element)

    for i in range( len(PARQUING_QUEUE) - 1):
        element = PARQUING_QUEUE.pop()
        print(i, "element", element[0].placa)
        
        if(element[0].placa == placa):
            print("\nSE RETIRA AUTO")
            print(f"Placa: {placa}")
            print("Auto retirado correctamente\n")

            return element, True
        element[3] += 1
        PARQUING_QUEUE.appendleft(element)

    print(f"\nAuto con placa {placa} no encontrado\n")
    return None,False
 
def cobrar(tiempo):
    return print(f"Precio: ${tiempo * PRECIO_MINUTO}")

def verificar_tiempo(inicio,final):
    if (final - inicio) > 30 : 
        print(f"MULTA: Te pasaste del tiempo tienes que pagar ${2 * PRECIO_MINUTO * 30} en vez de la tarifa normal" )
        return True
    return False

## simulación

# n = int(input("Ingrese la cantidad de PLACAS a generar: "))



## simulacion
print("""
    Detalles de la simulación
    1. Se generarán placas de autos aleatorias
    2. La simulación será instantanea, es decir, la ejecución de la simulación va a ser bastante rápido
    3. Habrá cierto porcentaje de probabilidad de que cada minutos llegue un auto, se vaya un auto o no pase nada.
""")
start_simulation = inquirer.confirm(message="Quieres iniciar una simulación ").execute()
sleep(.5)
if not start_simulation:
    exit(0)

time_choices = {
 "1 hora": 1,
 "3 horas": 3 ,
 "10 horas": 10 ,
 "24 horas": 24
}

choosed_time = inquirer.select(
    message="Por cuanto tiempo quieres hacer la simulacion del parqueadero: ",
    choices=["1 hora","3 horas","10 horas","24 horas"],
).execute()
sleep(.5)

probability_choises = [
        "33% de probabilidad de que llegue un auto, 33% de probabilidad de que se vaya un auto y  33% de probabilidad de que no pase nada.",
        "20% de probabilidad de que llegue un auto, 20% de probabilidad de que se vaya un auto y  60% de probabilidad de que no pase nada.",
        "50% de probabilidad de que llegue un auto, 50% de probabilidad de que se vaya un auto y  0% de probabilidad de que no pase nada."]

probability_choosed = inquirer.select(
    message="Que porcentaje de probabilidad habra que cada minuto llegue un auto, se vaya un auto o no pase nada.",
    choices=probability_choises
).execute()
sleep(.5)

probability = [0,0]

if probability_choises.index(probability_choosed) == 0: probability = [0,2]
elif probability_choises.index(probability_choosed) == 1: probability = [0,4]
elif probability_choises.index(probability_choosed) == 2: probability = [0,1]



iterations = (60 * time_choices[choosed_time] + 1)
spinner = yaspin(text=f"Generando {iterations} placas", color="yellow")
spinner.start()

PLACAS = generar_PLACAS(iterations)
i=1

spinner.text = f"{iterations} Placas generadas correctamente"
spinner.ok("✅ ")
spinner.stop()


spinner = yaspin(text="Simulando", color="yellow")
spinner.start()
sleep(2)


while HORA_ACTUAL < iterations:
    # aleatoriamente escoger si ingresa o retira un auto:
    print("\n---------------------------------------------------")
    print(f"Hora: { HORA_ACTUAL // 60} horas y {round(((HORA_ACTUAL / 60) % 1 ) * 60) } minutos" )
    automovil_placa = PLACAS.pop()

    ran = randint(probability[0],probability[1]) ## Hay un 10% de probabilidad de que entre un auto, 10% de que entre y 80% de que no pase nada
    if ran  == 0:
        tiempo = randint(0,40)
        ingresar_auto(placa=automovil_placa,tiempo_estadia=tiempo) 
        PLACAS_DENTRO.append(automovil_placa)
        
    elif ran == 1 :
        print("Se retirará un vehiculo")
        if len(PLACAS_DENTRO) != 0:
            auto_retirar = PLACAS_DENTRO[ randint(0, len(PLACAS_DENTRO) - 1) ]
            [car,success] = retirar_auto(auto_retirar)
            
            PLACAS_DENTRO.remove(auto_retirar)
    else:
        HORA_ACTUAL +=1
        print("No pasa nada")
        continue

    printQueue()
    HORA_ACTUAL +=1
spinner.text = "Simulacion terminada"
spinner.ok("✅ ")
spinner.stop()