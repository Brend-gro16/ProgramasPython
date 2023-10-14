#Crear un diccionario de llave numérica dias, con los siguientes elementos:
# 1- Lunes, 2 - Martes, 3 - Miércoles, 4 - Jueves, 5 - Viernes, 6 - Sabado, 7 - Domingo.
# Muestre el diccionario.
# Luego, accede y muestra:
# El primer elemento usando []
# El último elemento usando []
# El quinto elemento usando get()
# El séptimo elemento usando get()
# Muestre el diccionario completo.

import os; os.system('cls')

print('-----Crear---Acceder---Diccionario-----\n\n')
dias = {'1':'Lunes','2':'Martes','3': 'Miercoles','4':'Jueves','5':'Viernes','6': 'Sabado','7':'Domingo'}
print ('---Diccionario Completo---')
print(dias)

k1 = dias['1']
print(f'\n\nEl primer elemento es: {k1}')

k7 = dias['7']
print(f'El ultimo elemento es: {k7}')

print(f"El quinto elemento es: {dias.get('5')}")
print(f"El septimo elemento es: {dias.get('7')}")

