# Procesar una listas de nombres, une una lista original con una intriducida por el usuario

#Une dos listas de nombres
#Invierte la lista completa
#Convierte los nombres a mayúsculas


import os
os.system('cls')

print('----------Procesar lista de nombres ---------\n\n')

def procesa(n1, n2):
    res = []
    res.extend(n1)
    res.extend(n2)
    res.sort(reverse=True)
    
    for n in range(len(res)):
        res[n] = res[n].upper()
    return res

def leer():
    d = []
    while True:
     n = input('Nombre :')
     if n=='**': break
     d.append(n)
    return d

# Programa principal

nombres1 = ['Juan', 'Pedro', 'Luis', 'Jose', 'Maria']
print('Lista original:',nombres1, len(nombres1))
nombres2 = leer()
#nombres2=['Lucia','Angelica','Miguel']
print('\nLista nombres introducida:',nombres2, len(nombres2))

todos = procesa(nombres1, nombres2)
print('\nLista de todos:',todos, len(todos))