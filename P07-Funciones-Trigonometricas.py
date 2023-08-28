# Funciones trigonometricas en Python

import math

print('--Calculo de las funciones trigonometricas--\n')
 
angulo = float(input('Dame un angulo en grados: '))
gradosr =  math.radians (angulo)

seno     = math.sin(gradosr)
coseno   = math.cos(gradosr)
tangente = math.tan(gradosr)

# print(f'Seno:{seno} \n ,Coseno:{coseno}\n ,Tangente:{tangente}\n')

salida = ('Resumen de funciones\n'
f'El seno es {seno}\n'
f'El coseno es {coseno}\n'
f'La tangente es {tangente}\n'
f'El angulo {angulo} en radianes = {gradosr}\n')

print(salida)
