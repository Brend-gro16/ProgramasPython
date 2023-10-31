# Promedio el promedio de una lista de numeros luego crea una lista con los mayores al promedio

import os
os.system('cls')

print('----------Calcula Mayores Promedio ---------\n\n')


def leer ():
    lista = []
    while True:
        n = float (input('Numero:'))
        if n==1: break
        lista.append(n)
    return(lista)


def promedio (lista):
    s=0
    for n in lista:
        s+=n
    return s/ len(lista)

def maypresprom(lista, prom):
    mp = []
    for n in lista:
     if n > prom:
         mp.append(n)
    return mp

#Programa principal

#lista = [9,8,7,5,6,9,5,10,6,7]
lista= leer ()
print(lista, len (lista))
prom= promedio(lista)
print('\n**El promedio es:' ,prom)
mp = maypresprom(lista, prom)
print(f'\n**Los numeros mayores al promedio son : ',mp,len(mp))



