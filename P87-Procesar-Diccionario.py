#• Se tienen los datos de nombres y sueldos de los siguientes trabajadores, en dos listas:
#Nombres: Juan, Pedro, Manuel, Elias, Maria, Felipe, Julia, Roberto
#Sueldos: 4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00
#• Crear un diccionario con ambas listas
#• Mostrar el diccionario resultante
#• Iterar por los elementos del diccionario:
#o Usando las llaves : keys()
#o Usando los valores: values()
#o Usando la llave y el valor en base a la llave
#o Usando el para llave/valor items()
#• Obtener lo suma de los sueldos
#• Obtener el promedio de los sueldos.


import os; os.system('cls')

print('----------Procesar---Diccionario-----------\n\n')
nombres= {'Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto'}
sueldos={4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55,12234.00, 2000.00}
print ('Diccionario Inicial')

nomina = dict(zip(nombres, sueldos))
print(nomina)

print('\nIterar por Keys')
for k in nomina.keys():
    print(k) 
    
print('\nIterar por Valores')
for v in nomina.values():
    print(v) 
    
print('\nIterar por Llave y Valor')
for k,v in nomina.items():
    print(f'{k}   {v}')
    
s=p=0

for m,c in nomina.items():
    print(f'{m} - {c}')
    s=s+c
    
p=s/len(nomina)

print(f'\nLa suma de suledos es: {s:.3f} y el promedio de sueldos es: {p:.3f}')

