#• Cree un diccionario de llave de cadena municipios con los siguientes elementos:
#Apozol - 1863, Calera - 1868, Fresnillo - 1554, Guadalupe - 1821, Jalpa - 1824, Jerez - 1824, Loreto - 1931,
#Mazapil - 1824, Momax - 1857.
#• Mostrar el diccionario
#• Eliminar los elementos siguientes, en cada operación mostrar el diccionario:
#o Llave Apozol usando del
#o Llave Fresnillo usando pop()
#o Llave Momax usando popitem()
#o Borrar todos los elementos del diccionario con clear()
#• Mostrar diccionario.

import os; os.system('cls')

print('----------Eliminar---Diccionario-----------\n\n')
municipios= {'Apozol':'1863','Calera':'1868','Fresnillo': '1554','Guadalupe':'1821','Jalpa': '1824', 'Jerez': '1824', 'Loreto': '1931',
'Mazapil':'1824', 'Momax': '1857'}
print ('Diccionario Inicial')

print(municipios)

a = municipios.pop('Apozol')

print('\nEliminando a Apozol:')
print(municipios)

b = municipios.pop('Fresnillo')

print('\nEliminando a Fresnillo:')
print(municipios)

c = municipios.popitem()
print('\nEliminando a Momax:')
print(municipios)

municipios.clear()

print('\nSe elimino todo el diccionario:')
print (municipios)