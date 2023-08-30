# Calcular la Hipotenusa de un Triangulo

import math

print('\n---Calcula la hipotenusa de un triangulo---\n')

Acat= float (input('Escribe la longitud del cateto adyacente : '))
Ocat= float (input('Escribe la longitud del cateto opuesto :  '))

Hip= math.sqrt ((math.pow(Acat,2)+ math.pow(Ocat,2)))

Resultado=  (f'\nCateto adayacente =   {Acat}\n'
             f'Cateto opuesto =      {Ocat}\n\n')
           

print(Resultado)
print (f'---La hipotenusa es = {Hip:.3f}')
