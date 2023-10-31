
import os
os.system('cls')

print('----------Calcula el mayor y menor ---------\n\n')

def leer ():
    lista = []
    while True:
        n = float (input('Numero:'))
        if n==1: break
        lista.append(n)
    return(lista)

def menor (lista):
    m = lista[0]
    for n in lista: #Calcular el menor
        if n < m:
            m=n
    return m 

def mayor (lista):
    m = lista[0]
    for n in lista: #Calcular el menor
        if n > m:
            m=n
    return m 


#Programa principal
lista = leer()
#lista=[10,30,50,22,66,5,44]
print('\n',lista)

men=menor(lista)
print('\n**El menor es: ',men)
may=mayor(lista)
print('\n**El mayor es: ',may)


