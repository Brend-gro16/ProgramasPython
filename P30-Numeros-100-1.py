#Imprimir numeros del "n" al 1

import os

os.system ('cls')

print ('------Imprimiendo numeros del "n" al 1 (decremento)------')

n = int(input( '\n ¿Desde que numero deseas mostrar?: '))
#p = int(input( '\n ¿De cuanto en cuanto?: '))



c = n

while c >= 1:
      print(c, end=" ")
      c = c - 1

print ('\n\n *****Fuera del ciclo*****')
      
      