#Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988.
#Después modifique elementos como sigue:
#• Remplace 100 por 200
#• Remplace 999 por 1000
#• Remplace 988 por 999
#• Remplace el rango 123,456,222 por 555,666,777
#• Mostrar la lista resultante para comprobar
#La lista resultante: 200, 555, 666, 777, 1000, 895, 325, 234, 322, 999.*

import os
os.system('cls')


lista = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]

print('\n\n-------------Modificar lista-------------\n')

print(f'Los elementos iniciales son: {lista}\n')

lista [0]=200
lista [4]=1000
lista [-1]=999
lista[1:4] = [555,666,777]

print(f'La lista resultante es: {lista}')





