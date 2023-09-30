#Se desea imprimir los números de 1 a n de 10 en 10
#Dame número: 100
#Salida. 1 11 21 31 41 51 61 71 81 91

import os
os.system('cls')

print('\n\n-----Numeros de 1 a n (10 en 10)-----')
num= int(input('\n ¿Hasta que numero?:  '))

for i in range(1,num+1,10):
     print(f'{i}  ', end='')


    
    
