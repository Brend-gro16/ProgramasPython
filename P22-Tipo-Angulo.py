#Verificar el tipo de angulo 
#< 90 agudo, = 90 recto, > 90 y <180 obtuso,  = 180 llano, >180 < 360 concavo, = 360 completo

import os

os.system ('cls')

print ('---Verificar el tipo de angulo--- ')
angulo = int(input('\n Introduce el angulo: '))

if angulo >=0 and angulo <=360:
    print ('                 ...')
    if angulo < 90:
        print ('          --Angulo agudo--')
    elif angulo == 90:
        print ('          --Angulo recto--')
    elif angulo >90 and angulo <180:
        print ('          --Angulo obtuso--')
    elif angulo == 180:
        print ('          --Angulo llano--')
    elif angulo >180 and angulo <360:
        print ('          --Angulo concavo--')
    else:
        print ('          --Angulo completo--')    
        
else:
    print ('***Angulo fuera de rango***')    