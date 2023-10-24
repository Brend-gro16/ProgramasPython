#Funcion con parametros

import os
os.system('cls')


print('----------Funcion-Parametro-----------\n\n')

def saluda(nombre,edad):
    print(f'Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres y tu edad es {edad}.')

#Programa principal
saluda('Carlos Castaneda',30)
saluda('Juan Perez Diaz',10)
saluda('María Soto García',25)
saluda('AMLO',76)

#print(nombre)---Los parametros no son accesibles fuera de la funcion