##Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo,
##2 es lunes y así hasta 7 es sabado. Si el número no está en el rango especificado, mostrar un mensaje de error.

import os

os.system ('cls')

print ('---Correspondencia entre numero y dia de la semana--- \n ')

dia = int(input('\n Introduce un numero (0-7): '))

if dia == 1:
    print (' \n****DOMINGO**** \n ')
elif dia == 2:
    print ('\n****LUNES**** \n ')
elif dia == 3:
    print ('\n****MARTES**** \n ')
elif dia == 4:
    print ('\n****MIERCOLES**** \n ')
elif dia == 5:
    print ('\n****JUEVES**** \n ')
elif dia == 6:
    print ('\n****VIERNES**** \n ')
elif dia == 7:
    print ('\n****SABADO**** \n ')
    
else:
    print('\n\n +++El numero introducido esta fuera del rango+++')
    
    
    
    

