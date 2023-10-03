
# Iterar sobre los elementos de la lista

import os
os.system('cls')

print ('\n\n-----Iterar sobre los elementos de la lista-----\n')

nums = [2, 4, 6, 8, 10, 12, 14, 16]

print(f'Todos los números : {nums}')

print('\n\n--Iterar por elementos--')
for num in nums:
    print(num, end=' ')

print('\n\n-Iterar por indice-')
for i in range(len(nums)):
    print(nums[i], end=' ')

print('\n\n-Iterar por elementos sumando 2-')
for n in nums:
    print(n+2, end= ' ')

print('\n\n-Iterar por indice sumando 10-')
for i in range(len(nums)):
    print(nums[i]+10, end= ' ')
    
print(f'\n\n\n {nums}')