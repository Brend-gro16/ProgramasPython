#Verificar la segunda Ley de Newton (F= ma )

import os

os.system ('cls')


print ('---------------Ley de Newton---------------\n')
print ('[F]uerza         f = m * a ')
print ('[M]asa           m = f / a')
print ('[A]celeracion    a = f / m ')

op= input ('Elige ? ').upper()

if op == 'F':
    print ('\n--Calculando la Fuerza-- \n')
    m = float(input('Dame la masa: '))
    a = float(input('Dame la aceleracion: '))
    f = m *a 
    print (f'\n\n La fuerza calculada es: {f:.2f} ')
elif op == 'M':
    print ('\n--Calculando la Masa-- \n')
    f = float(input('Dame la fuerza: '))
    a = float(input('Dame la aceleracion: '))
    m = f / a 
    print (f'\n\n La masa calculada es: {m:.2f} ')
elif op == 'A':
    print ('\n--Calculando la Aceleracion-- \n')
    f = float(input('Dame la fuerza: '))
    m = float(input('Dame la masa: '))
    a = f / m 
    print (f'\n\n La aceleracion calculada es: {a:.2f} ')
    
print ('\n          ***Proceso terminado***')
    
    
