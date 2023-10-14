#Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988.
#Después, acceda y muestre:
#• El primero elemento
#• El último elemento
#• El elemento : 999
#• Los elementos entre: 123 a 999
#• Los elementos desde el inicio hasta el 222
#• Los elementos desde 222 hasta el final
#• Los tres úlitmos elementos usando índice negativo

import os
os.system('cls')


lista = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]

print('\n\n-------------Acceder a lista-------------\n')

print(f'Los elementos son: {lista}\n')

print(f'El primer elemento es: {lista[0]}\n')
print(f'El ultimo elemento es: {lista[-1]}\n')
print(f'El elemento 999 : {lista[4]}\n')
print(f'El elemento del 123 al 999: {lista[1:5]} \n')
print(f'Elementos del incio al 222: {lista[:4]} \n')
print(f'Elementos del 222 al final: {lista[4:]} \n')
print(f'Los 3 ultimos con indice negativo: {lista[-3:]}\n')





