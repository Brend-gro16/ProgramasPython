#Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee:
#Dame número ? 4
#Salida:
#1
#2 2
#3 3 3
#4 4 4 4

import os
os.system('cls')

print('\n\n-----Imprime la pirámide de un caracter----- \n')

n = int(input('Numero de renglones: '))


for i in range(1,n+1):
    
    for j in range(1,i+1):
        
        print(i, end=' ')
    print('\r')