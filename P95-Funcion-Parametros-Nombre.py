#funcion que al ser invocada usa el nombre del parametro


import os
os.system('cls')


print('----------Funcion-Parametros-Nombre-----------\n\n')

def saluda(apaterno,amaterno,nombre):
    print(f"Paterno:{apaterno}\nMaterno: {amaterno}\nNombre: {nombre}")
    print('-'*20)


saluda("Del Rio","Guerrero","Brenda")
saluda(nombre="Brenda",apaterno="Del Rio",amaterno="Guerrero")
saluda(amaterno="Guerrero",nombre="Brenda",apaterno="Del Rio",)
