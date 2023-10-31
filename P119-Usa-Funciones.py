#Uso de funciones programa P118

import os
os.system('cls')

print('----------Uso de Funciones ---------\n\n')


import P118Funciones as pf

l1= pf.leer ()
may=pf.mayor (l1)
men=pf.menor(l1)
suma=pf.suma(l1)
promedio=pf.promedio(l1)

print('La lista es:',l1)
print('El menor es:',men)
print('El mayo es:',may)
print('La suma es:',suma)
print('El promedio es:',promedio)

