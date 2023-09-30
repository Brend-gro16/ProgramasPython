#Calcular el factorial de un numero

import os
os.system('cls')


print('\n-----Calcula el factorial de un número----- \n')

h = int(input('\n ¿De que numero quieres calcular el factorial?:  '))
f = 1

for h in range(1,h+1):
    
    print(h, end= "*")
    f = f * h

#print ("=",f)
print(f'\n\n    ****El factorial es: {f}****')