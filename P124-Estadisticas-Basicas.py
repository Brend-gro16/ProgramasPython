#Se crea una función que lee un arreglo de números enteros (ya la hicimos en clase)
#• Crear una función para cada una de las siguientes estadísticas (poblacional):
#o Mayor
#o Menor
#o Media
#o Varianza
#o Desviación estánda
#• Se muestran los resultados de cada operación.

#Dame números: 5 6 6 7 8 9 10 10
#Lista de números: [5, 6, 6, 7, 8, 9, 10, 10]
#La media: 7.625
#Mayor de los datos: 10
#Menor de los datos: 5
#Varianza: 3.234
#Desviación estándar: 1.798

import os
import math
os.system('cls')

print('----------Estadisticas Basicas ---------\n\n')
from math import sqrt


#------------------------------Funciones
def leer():
    lista=[]
    while True:
        n=int(input("Dame numeros:"))
        if n==0:
            break
        lista.append(n)
    return lista

def suma(lista):
    s = 0
    for n in lista:
        s += n
    return s

def mayor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] > m :
            m = lista[n]
    return m

def menor(lista):
    m = lista[0]
    for n in range(len(lista)):
        if lista[n] < m :
            m = lista[n]
    return m

def media(lista):
    m = 0
    for n in lista:
        m += n
    m=m / len(lista)
    return m

def var(lista):
    m = 0
    for n in lista:
        m += n
    m=m/len(lista)
    v=0
    for n in lista:
        v += (n-m)**2
    v=v/len(lista)
    return v 

def des(lista):
    m = 0
    for n in lista:
        m += n
    m=m/len(lista)
    v=0
    for n in lista:
        v += (n-m)**2
    v=v/len(lista)
    d=sqrt(v)
    return d

#------------------------Programa Principal

lista=leer()
print ("\n---------Lista de numeros---------\n",lista)

may = mayor(lista)
men = menor(lista)
med = media(lista)
varianza=var(lista)
de=des(lista)

print(f"\n***La media: ",med )
print(f"\n***Mayor de los datos: ", may)
print(f"\n***Menor de los datos:", men)
print(f"\n***Varianza: {varianza:.3f}")
print(f"\n***Desviacion Estandar: {de:.3f} ")
