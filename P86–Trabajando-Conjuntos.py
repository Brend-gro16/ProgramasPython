#Nos permite ejemplificar las operaciones basicas con conjuntos

import os; os.system('cls')


print('----------Operaciones Basicas en Conjuntos\n\n')

muns= {'Zacatecas', 'Guadalupe', 'Jerez', 'Fresnillo'}

print(muns,len(muns),type(muns))

for mun in muns:
    print(mun, end = ' ')
    
muns.add('Teul')
print('\n',muns, len(muns))

muns.update ({'Luis Moya','Ojocaliente', 'Tepetongo'})
print('\n',muns, len(muns))

muns.remove('Zacatecas')
print('\n',muns, len(muns))

muns.discard('Canitas')
muns.discard('Ojocaliente')
print('\n',muns, len(muns))

print('Luis Moya' in muns)


#--------Otra forma de saber si esta
if ('Luis Moya' in muns):
    print('\nSi esta')
else:
    print('\nNo esta')
    
muns.pop()
print(muns, len(muns))


#Eliminar todo
muns.clear()
print(muns, len(muns))


