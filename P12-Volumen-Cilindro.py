#Calcular el volumen de un cilindro

import math 

print ('-----Calcular el volumen de un cilindro-----\n ')
radio = float (input('Introduce el radio: '))
altura = float(input('Introduce la altura: '))

vol= (math.pi * (math.pow(radio,2))) * altura 

print(f'\n\n El volumen del cilindro con radio =  {radio}, y altura = {altura} es: {vol:.3f}')