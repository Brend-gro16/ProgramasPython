# Funcion con parametros con valores por defecto o valores pre esstablecidos

import os
os.system('cls')

print('----------Funcion-Parametros-Por--Defecto-----------\n\n')

def saluda(nombre="Chris",edad=14):
    print(f"Hola {nombre} tu edad es {edad}")

saluda()
saluda("Chris")
saluda("Brenda",150)