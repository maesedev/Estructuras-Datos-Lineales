from random import randint, choice

"""
Un docente maneja la lista de estudiantes y calificaciones mediante arreglos
unidimensionales, en un arreglo de tipo entero guarda los códigos, en uno de tipo cadena, los
nombres; y en un arreglo bidimensional de cuatro columnas guarda las notas: corte 1, cort2 y
cort3 y la definitiva. La definitiva se calcula así: definitiva = (parcial1*30% +parcial2*30% +
parcial3*30%).
"""

def ordenar_nota_ascendente(nombres, codigos, notas):
    nb = len(codigos)
    

    for actual in range(0,nb):
        
        mas_grande = actual
        
        for j in range(actual + 1 ,nb) :
            
            if notas[j][3] > notas[mas_grande][3] :
                mas_grande = j
                
        if mas_grande is not actual :
            
            nombre_temp = nombres[actual] 
            nombres[actual] = nombres[mas_grande]
            nombres[mas_grande] = nombre_temp
            
            
            codigo_temp = codigos[actual] 
            codigos[actual] = codigos[mas_grande]
            codigos[mas_grande] = codigo_temp
            
            
            notas_temp = notas[actual] 
            notas[actual] = notas[mas_grande]
            notas[mas_grande] = notas_temp

N = randint(5,10) 

nombres_aleatorios =["Juan", "Pedro", "Luis", "Carlos", "Andrés","María", "Ana", "Sofía", "Lucía", "Valentina"]

codigos = []
notas = [[]]
nombres = []

for i in range (0,N):
    
	codigos.insert( i , f"A-50{i + 1}" )
	for j in range(0,3):
	    notas[ i ].append(  randint(20,50) / 10  )
	    
	definitiva = (notas[i][0] * .3) +(notas[i][1] * .3) +(notas[i][2] * .4)   
	
	notas[i].append(definitiva )
	notas.append([])
	
	nombres.insert(i, choice(nombres_aleatorios) )

	"""
	print(f"Notas del estudiante A-50{i + 1} ")
    
	print(f"Corte 1: \t{notas[i][0]} ")
	print(f"Corte 2: \t{notas[i][1]} ")
	print(f"Corte 3: \t{notas[i][2]} ")
	print(f"Definitiva: \t{notas[i][3]} \n")"""
	

ordenar_nota_ascendente(nombres, codigos, notas)
print("\n\n-----------------------------")
for i in range(0,N):
    
    print(f"Notas del estudiante {codigos[i]} ")
    print(f"Corte 1: \t{notas[i][0]} ")
    print(f"Corte 2: \t{notas[i][1]} ")
    print(f"Corte 3: \t{notas[i][2]} ")
    print(f"Definitiva: \t{notas[i][3]} \n")
