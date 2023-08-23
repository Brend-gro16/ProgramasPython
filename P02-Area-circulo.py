#Calcular el area de un circulo

import math #Importar libreria de funciones y constantes matematicas 

print('Calcular el area de un circulo: \n')


radio = float(input('Dame el radio: '))
area = math.pi * math.pow(radio,2)

print (f'\nEl circulo de radio {radio} tiene un area de {area:.2f}')