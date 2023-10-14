# Calificaciones

import os
os.system('cls')

print('---------------CALIFICACIONES--------------\n\n')

materias = ['Fisica', 'Quimica', 'Matematicas','Geografia', 'Estadistica']

califs = [10, 9, 8, 7.5, 6]

print(f'---Lista de materias--- \n{materias}\n')
print(f'---Lista de calficaciones--- \n{califs}\n')

notas = dict(zip(materias, califs))

print(f'\nLas notas:', notas,len(notas))
notas.update({'Ingles':10})
notas.update({'Programacion':7})
print(f'\nDiccionario actualizado:', notas,len(notas))

notas.pop('Fisica')
notas.popitem()
print(f'\nDiccionario actualizado:', notas,len(notas))

notas.update({'Quimica':10}) #notas [Quimica] = 10}
notas.update({'Matematicas':10})
print(f'\nDiccionario actualizado:', notas,len(notas))

s=p=0

for m,c in notas.items():
    print(f'{m:<12} - {c:>5.2f}')
    s=s+c
    
p=s/len(notas)

print(f'\nLa suma es: {s} y el promedio es: {p}')

