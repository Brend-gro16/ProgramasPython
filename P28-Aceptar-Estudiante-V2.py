#Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. La
#Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5.

import os

os.system ('cls')


print ('++++++  Universidad Kitty Kat SA  +++++++')
print ('\n\n----Verificacion de estudiantes---')

nombre = input('\nDame tu nombre: ')
edad = int(input('\nDame tu edad: '))
sexo = int(input ('\nSexo:  (1) mujer...(2)hombre: '))

if edad > 21 and sexo == 1:

    print('\n\ncontunuamos...')
    
    c1 = float(input('\n Introduce la calificacion 1: '))
    c2 = float(input('\n Introduce la calificacion 2: '))
    c3 = float(input('\n Introduce la calificacion 3: '))
    prom= (c1 + c2 + c3)/3
    if prom > 8 and prom <9.5:
        print (f'\n\n---------- Bienvenid@ {nombre} tu promedio es {prom:.2f}')
    else:
        print (f'\n\n Tu promedio es {prom:.2f}---Solo aceptamos promedio entre 8 y 9.5---')
else:
    edad < 21
    print ('\n\n---Solo aceptamos MUJERES mayores de 21 años---')
    
print ('\n                 ***Proceso terminado**')
 