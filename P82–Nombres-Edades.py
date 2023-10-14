# Nombres y edades

import os
os.system('cls')

datos = {}

print('-----Nombres y Edades-----\n\n')
print('Introduce nombres y edades (* en el nombre para terminar)')

while True:
    nombre = input('Nombre   : ')
    if nombre=='*':
        break
    else:
         datos[nombre]=int(input('Edad     : '))

print(f'Los datos introducidos son:\n', datos, len(datos))

print('\nListado y edades:')

s=p=0

for n,e in datos.items():
    print(f'{n:<20} - {e:3}')
    s=s+e
p= s/ len(datos)

print(f'\n\nSuma:  {s} \nPromedio:{p}')

