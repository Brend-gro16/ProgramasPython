# Remover elementos de la lista


import os
os.system('cls')

print('\n\n-----Remover elementos de la lista-----')

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]

print(f'\nTodos los números : {nums}\n')
print(f'El total de elementos son: {len(nums)}')


print('\n-Remueve el valor "99" de la lista')
nums.remove(99)
print(nums)

print('\n-Remueve el elemento de la posicion 8')
num=nums.pop(8) 
print(nums)


print('\n-Quita el ultimo elemento')
num=nums.pop()

print(nums)


print('\n-Quita todos los elemento')
nums.clear() 

print(nums)
