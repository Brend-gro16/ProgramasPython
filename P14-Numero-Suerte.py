# Numero de la suerte



#*****************Este programa presenta el problema de la multiplicacion x cero *****

import math

print('\n\n--Numero de la Suerte--\n\n')

año = int(input('Introduce el año de nacimiento (4 cifras, hasta 1999): '))

d1 = math.trunc(año/1000)                 
d2 = math.trunc( (año / 100) - 10)
d3 = math.trunc((año - (d1*1000) - (d2*100)) /10)
d4 = año - (d1*1000)-(d2*100)- (d3*10)

 
sum = d1 + d2 + d3 + d4 


print (f'La suma de {d1}, {d2}, {d3}, {d4}...')

print(f'\n\n*****El numero de la suertes es: {sum} *****')
