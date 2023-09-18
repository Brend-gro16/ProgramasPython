# Imprime las tablas de 1 a n, hasta m


import os


           
while(True):
    os.system('cls')
    print ('-----Tablas de Multiplicar-----\n\n')
    n = int(input('¿Hasta que tabla?:  '))
    m = int(input('\n¿Hasta donde?: '))     
    t = 1 
    while t <= n:
        print(f'\nTabla del {t} \n') 
        c=1
     
        while( c <= m ):
            print(f'{t} x {c} = {t*c}')
            c+=1  
        t = t + 1 
    res=input('\nDeseas Continuar(S/N)? ')
    if res.upper()=='N': break

print("\n\n***Fin del Proceso****")