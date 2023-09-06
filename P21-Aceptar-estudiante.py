#Aceptar a un estudiante en base a la edad y sus calificaciones

import os

os.system ('cls')

print ('----Verificacion de estudiantes---')

nombre = input('\nDame tu nombre: ')
edad = int(input('Dame tu edad: '))

if edad > 18:
    print('contunuamos...')
    print ('Dame 2 calificaciones (0-10) separadas por un enter: ')
    c1, c2 = int(input()),int (input())
    if c1>=8 and c2>=8:
        print (f'---------- Bienvenid@ {nombre} tus calificaiones son {c1} y {c2}')
    else:
        print ('Solo aceptamos calificaciones > 8')
else:
    edad < 18
    print ('Solo aceptamos mayores de 18 años')
    
print ('\n ***Proceso terminado**')
 