#Calcula la suma de una lista de numeros usando una funcion

import os
os.system('cls')

print('----------Suma de una lista de numeros ---------\n\n')

def suma(lista):
    s = 0
    for n in lista:
        s += n
    return s


##Progrma Principal

#lista = [10, 20, 30, 40, 50,60,70,80,90,100]
lista = [10, 20, 30, 40, 50]
res = suma(lista)
print('La suma es ', res)

