# Crear un  Modulo con las Funciones

def mayor (lista):
    m = lista[0]
    for n in lista: #Calcular el menor
        if n > m:
            m=n
    return m 

def menor (lista):
    m = lista[0]
    for n in lista: #Calcular el mayor
        if n < m:
            m=n
    return m 

def promedio (lista):
    s=0
    for n in lista:
        s+=n
    return s/ len(lista)

def suma(lista):
    s = 0
    for n in lista:
        s += n
    return s


def leer ():
    lista = []
    while True:
        n = float (input('Numero:'))
        if n==1: break
        lista.append(n)
    return(lista)

