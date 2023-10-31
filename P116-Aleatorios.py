#Se generan dos listas de numeros aleatorioas y se suman


import random


import os
os.system('cls')

print('----------Calcula Numeros Aleatorios y los suma ---------\n\n')

MAX = 20

def generaAleatorios():
    l = []
    for n in range (MAX):
        l.append( random.randint(1,100))
    return l

def sumalistas(l1, l2):
    suma = []
    for i in range(MAX):
     suma.append( l1[i] + l2[i] )
    return suma

# Programa principal
l1 = generaAleatorios()
l2 = generaAleatorios()
suma = sumalistas(l1, l2)

print(f'\nLista 1 : ',l1,len(l1))
print(f'Lista 2 : ',l2,len (l2))
print(f'\nLa suma de las listas es:\n   ',suma, len(suma))