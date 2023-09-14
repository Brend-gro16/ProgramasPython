#Imprimir numeros del 1 al "n"

import os

os.system ('cls')

print ('------Imprimiendo numeros del 1  a "n" ------')
n = int(input( '\n ¿Hasta que numero deseas mostrar?: '))
p = int(input( '\n ¿De cuanto en cuanto?: '))



c = 1

while c <= n:
      print(c, end=" ")
      c = c + p