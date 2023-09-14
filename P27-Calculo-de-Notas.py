#Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar el resultado e imprimir
#un mensaje de acuerdo al promedio obtenido:

import os

os.system ('cls')

print ('---Calculo de Notas--- \n ')


nota1 = float(input('\n Introduce la nota 1: '))
nota2 = float(input('\n Introduce la nota 2: '))
nota3 = float(input('\n Introduce la nota 3: '))
nota4 = float(input('\n Introduce la nota 4: '))
nota5 = float(input('\n Introduce la nota 5: '))


suma = nota1 + nota2 + nota3 + nota4 + nota5
prom = suma /5

print (f'\n --Tu promedio es {prom:.2f}--')

if prom > 0 and prom <= 6:
    print (' \n\n****Quedas REPROBADO****')
elif prom > 6 and prom <= 7:
    print (' \n\n****Pasas de Panzazo****')
elif prom > 7 and prom <= 8:
    print (' \n\n****Muy bien, puedes mejorar****')
elif prom > 8 and prom <= 9:
    print (' \n\n****Exelente, sigue asi****')
elif prom > 9  and prom <= 10:
    print (' \n\n****Pasas de Panzazo****')
else:
    print ('\n +++ERROR+++')
    
    
    