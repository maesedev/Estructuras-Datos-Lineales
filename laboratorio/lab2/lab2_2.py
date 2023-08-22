from modules.linked_list import ListaEnlazada
from modules.robot import Robot
from random import randint

def app():
    listaRobots = crearRobots()
    imprimir_robots(listaRobots)
    robotsEnergicos(listaRobots)
    res = ""
    res = robotsPerezosos(listaRobots,res,0)
    print("\n\n Los 3 menos energeticos",res)
    disminuir_batería(listaRobots)


def crearRobots():
    """Creación de los robots"""
    robotsList = ListaEnlazada()

    ID = 0
    for _ in range (randint(10,20)):
        bat = randint(10,100)
        robot = Robot(ID=ID,bateria=bat,tipo="Mecánico") 
        ID+=1

        if robotsList.is_empty():
            robotsList.add_at_start(robot)
            continue

        for j in range(robotsList.size()):
            robot_actual = robotsList.get(j)
            if robot_actual.bateria > robot.bateria:
                robotsList.add_between(j, robot)
                break
            if  robot_actual.bateria < robot.bateria and j == robotsList.size():
                robotsList.add_at_end(robot)
                break
    return robotsList

def imprimir_robots(lista):
    texto = "\n"
    for i in range(lista.size()):
        
        texto += f"ID: { lista.get(i).ID}  \n"
        texto +=f"Tipo:  {lista.get(i).tipo}\n"
        texto +=f"Bateria:  {lista.get(i).bateria}%\n\n"

    print(texto)

def robotsEnergicos(robots):

    print("Robots con mas de 60% de bateria")
    for i in range(robots.size()):
        curr_robot = robots.get(i)
        if curr_robot.bateria > 60:
            print("\nID: ", curr_robot.ID)
            print("Tipo: ", curr_robot.tipo)
            print("Batería: ", curr_robot.bateria,"%")



def robotsPerezosos(robots,res,i):
    if i == 3:
        return res
    res  +=  f"\n\nID: {robots.get(i).ID} \nTipo:{robots.get(i).tipo} \nBatería: {robots.get(i).bateria}%  {robotsPerezosos(robots, res , i + 1)}"
    return res
    

def disminuir_batería(robots):
    edited = 0
    for i in range(robots.size()):
        robot = robots.get(i)

        if robot.bateria > 30 and robot.bateria < 50:
            robots.edit( i , robot.bateria - 15)
            edited += 1
    print(f"Se le redujo 15% de bateria a {edited} robots")
        


app()