from collections import deque
from InquirerPy import inquirer

d = deque(maxlen=3)

d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.append(6)
print(d)


name = inquirer.text(message="What's your name:").execute()

time = inquirer.select(
    message="Por cuanto tiempo quieres hacer la simulacion del parqueadero: ",
    choices=["30 minutos","1 hora","10 horas","24 horas"],
).execute()

print(time)