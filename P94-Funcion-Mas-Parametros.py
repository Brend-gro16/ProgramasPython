#Funcion que recibe un numero arbitrario de parametros

import os
os.system('cls')


print('----------Funcion-Mas-Parametros-----------\n\n')

def saludatodos(*todos):
    print(f"\nSaludos a {todos}")
    
    for nombre in todos:
        print('Hola',nombre)
        
    if (len(todos)!=0):    
        print(f" \nEl primero es el primero y es: {todos[0]}")
        print(f" \nEl ultimo es el ultimo y es: {todos[-1]}")
    
saludatodos("Jose","Juan","Pedro","Luis","Rocio","Fatima","Maria","Felipe","Mercedes")