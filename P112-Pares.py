
import os
os.system('cls')

print('----------Pares ---------\n\n')

def pares(lista):
    p =[]
    for n in lista:
        if n%2 == 0:
            p.append (n)
    return (n)

def leer ():
    lista = []
    while True:
        n = float (input('Numero:'))
        if n==1: break
        lista.append(n)
    return(lista)


#Programa Principal
 
#lista = [1,2,3,4,5,6,7,8,9,10]
lista = leer ()
print (lista,len(lista))
res=pares(lista)
print('La lista con los pares es: ', res)