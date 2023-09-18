# Imprime la tabla de multiplicar deseada del 1 al n ciclo while


import os

while(True):
    os.system('cls')
    
    print ('-----Tablas de Multiplicar-----')
    
    t = int(input('\n\nTabla del: '))
    n = int(input('¿Hasta que numero llegara la tabla?:  '))
    c = 1
    
    while( c <= n):
       print(f'{t} x {c} = {t*c}')
       c+=1
    res=input('\n\nDeseas Continuar(S/N)? ')
    if res.upper()=='N':
        break

print("\n\n***Fin del Proceso****")