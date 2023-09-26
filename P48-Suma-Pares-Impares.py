# Numeros pares e impares y su suma en el rango de 1 a n

import os
while(True):
    os.system('cls')
    
    print('-----Pares e impares de 1 a n y su suma----- \n')
    n = int(input('¿Hasta donde deseas imprimir?: '))
    s = 0
    
    print("\n--Numeros pares---")
    
    for par in range(2,n+1,2):
        print(par,end=' ')
        s += par
        
    print(f'\n\n\t--Suma numeros pares: {s}')
        
    s=0    
    print("\n--Numeros impares--")
    
    for impar in range(1,n+1,2):
        print(impar,end=' ')
        s += impar
        
    print(f'\n\n\t--Suma numeros impares: {s}')
        
    res = input('\n\nDeseas continuar (S/N) ? ').upper()
    if res=='N':
        break
print('\n\n*****FIN DEL PROCESO*****')