## Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, si no lo son
## (1,4,6) mandar mensaje de error.

import os

os.system ('cls')

print ('---Verificar si los numeros son consecutivos--- \n ')

num1 = int(input('\n Introduce el numero1: '))
num2 = int(input('\n Introduce el numero2: '))
num3 = int(input('\n Introduce el numero3: '))


if num1 + 1 == num2 and num1 + 2 == num3:
    print ('\n...Los numeros SON CONSECUTIVOS...')
      
else:
    print ('\n...Los numeros NO SON consecutivos...')    
    