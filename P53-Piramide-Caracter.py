##Imprime una piramide de un caracter determinado, usando dos ciclos fo anidados

import os
os.system('cls')

print('\n\n-----Imprime la pirámide de un caracter----- \n')

n = int(input('Numero de renglones: '))
c = input('Caracter:')

for i in range(1,n+1):
    
    for j in range(1,i+1):
        print(c, end='')
    print('\r')