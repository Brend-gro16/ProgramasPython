# Agregar elementos a la lista

import os
os.system('cls')

print('\n\n-----Agregar elementos a una lista existente----- \n')

nums = [80.3, 12.5, 60.2, 30.4]
otros = [110,120, 130]


print(f'Valores iniciales : {nums},{len(nums)} \n')

nums.append(90) #se agredo un 90 al final de  la lista
nums.append(100)# se agrego un 100 al final de la lista
print(f'Agregar al final : {nums}\n')

nums.insert(4,80) #inserto un 80 en la posicion 4
print(f'Insertar : {nums}\n')

otros = [110,120,130]
nums.extend(otros)
print(f'extender con : {nums}\n')