#• Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
#• Se crea una función que suma los dígitos individuales de un número (ya la hicimos en clase)
#• Se crea una función que recibe las lista capturada, usa la función anterior (suma dígitos) y recorre la lista
#de números y suma sus dígitos, y regresa una lista con las sumas de los dígitos de los números de la lista.
#• Se imprime la lista original y la lista con las sumas de los dígitos de los números capturados.

#Dame los números: 1971 2345 2015 2022
#La lista de números original : [1971, 2345, 2015, 2022]
#La lista con las suma de dígitos de los números: [18, 14, 8, 6]

import os
import math
os.system('cls')

print('----------Suma Digitos Lista ---------\n\n')

def leer():
    lista=[]
    while True:
        n=int(input("Numero:"))
        if n==0:
            break
        lista.append(n)
    return lista

def sumadigitos(n):
    listaSum=[]
    for n in lista:
        suma = 0
        for d in str(n):
            suma += int(d)
        listaSum.append(suma)
    return listaSum

lista=leer()
print ("\n---Lista original: ",lista)

suma=sumadigitos(lista)
print("---La lista con las suma de dígitos de los números:  ",suma)
