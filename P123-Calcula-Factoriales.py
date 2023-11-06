#• Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
#• Se crea una función que calcula el factorial de un número (ya la hicimos en clase)
#• Se crea una función que recibe las lista capturada, usa la función anterior (calcular factorial) que recorre la
#lista de números y calcula el factorial de cada uno de ellos, y regresa como resultado una lista con los
#factoriales de los números de la lista.
#• Se imprime la lista original y la lista con los factoriales de los números capturados.
#
#Dame los números: 2 5 8 9
#La lista de números originales: [2, 5, 8, 9]
#La lista con los factoriales: [2, 120, 40320, 362880]


import os
import math
os.system('cls')

print('----------Calcula Factoriales ---------\n\n')

def leer():
    lista=[]
    while True:
        n=int(input("Numero:"))
        if n==0:
            break
        lista.append(n)
    return lista

def factorial(n):
    listafac=[]
    for n in lista:
        fac=1
        for d in range(1,n+1):
            fac*=int(d)
        listafac.append(fac)
    return listafac

lista=leer()
print ("----\nLa Lista de numeros originales:",lista)

factor=factorial(lista)
print(f"La lista con los factoriales",factor)

