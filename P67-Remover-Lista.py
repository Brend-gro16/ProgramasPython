#Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988.
#Después remover elementos como sigue:
#• Remover con de los elementos 100, 123, 456
#• Remover con remove() los elementos 322, 988
#• Remover con pop() el elemento 222 y mostrarlo
#• Remover con pop() el último elemento hasta ahora y mostrarlo
#• Mostrar la lista resultante para comprobar
#Considere que la lista va ir perdiendo elementos, para que considere las posiciones a utilizar en los comandos
#anteriores.
#La lista resultante: 999, 895, 325
#• Remover con clear() todos los elementos, resultando una lista vacia.

import os
os.system('cls')


lista = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]

print('\n\n-------------Remover lista-------------\n')

print(f'Los elementos iniciales son: {lista}\n')

lista.remove(100)
lista.remove(123)
lista.remove(456)

lista.remove(322)
lista.remove(988)
print (f'La lista hasta ahora es: {lista}\n')

lis=lista.pop (0)
print(lis)

ultimo= lista.pop()
print(ultimo)

print(f'\nLa lista resultante es: {lista}')



  


  
