#Dados tres números enteros, verificar cual es el mayor

import os

os.system ('cls')

print ('---Verificar que numero es mayor--- \n ')

num1 = int(input('\n Introduce el numero1: '))
num2 = int(input('\n Introduce el numero2: '))
num3 = int(input('\n Introduce el numero3: '))

if num1 > num2 and num1 > num3 :
    print (f'\n\n---{num1} es el numero mayor---')
elif num2 > num1 and num2 > num3:
    print (f'\n\n---{num2} es el numero mayor---')
elif num3 > num1 and num3 > num2:
    print (f'\n\n---{num3} es el numero mayor---')

else:
    print ('\n\n***Algunos numeros son iguales***')    
    