# Cambiar los elementos de una lista

import os
os.system('cls')

nums = [10.0, 9.0, 8.5, 6.5, 9.8, 7.0, 5.0, 6.2, 9.5]

print(f'\n\n-----Cambiar los elementos de una lista-----')
print(f'\nTodos los números: {nums}\n')

print(type(nums))

nums[0]=7
nums[1]=7
print(nums) #se modifico 0 y 1
nums[2:5] = [9.0,9.0,9.0] #se modifico del 2-4
print(nums)
nums[-1] = 6.0 # se modifico el ultimo 
print (nums)
nums[6] =nums[6] + 5.0 # se sumo 0.5 al lugar 6
print (nums)


