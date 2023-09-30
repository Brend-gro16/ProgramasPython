#Imprimir las tablas del 1 a n, desde 1 hasta m


import os
os.system('cls')


print('\n\n----Tablas de Multiplicar de la tabla 1 a la tabla n-----')

n = int(input('\n¿Hasta que tabla?:  '))
m = int(input('¿Hasta que numero?:  '))

for i in range(1,n+1):
    print(f'\nTabla del {i}\n')
    for j in range(1,m+1):
        print(f'{i} x {j} = {i*i}')
        print('\n')