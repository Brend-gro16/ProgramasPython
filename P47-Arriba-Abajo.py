# Imprimir numeros ascendiente o descendente 



import os
while(True):
    
    os.system('cls')
 
    
    print('\n----Imprimir los numeros ascendente o descendente----')
    
    print('[1] Imprimir los números de 1 a n ')
    print('[2] Imprimir los numeros de n a 1 ')
    
    op = int( input('\nElige una opción ? ') )
    
    
    if op==1:
        print('\nImprimiendo los numeros de 1 hasta n \n')
        n = int(input('\nHasta que numero (n)?: '))
        print(f'\n---Numeros de 1 hasta {n} \n')
        for x in range(1,n+1,1):
         print(x,end=' ')

    elif op==2:
        print(f'\n-----Imprimiendo los numeros de n hasta 1----- \n')
        n = int(input('\n¿Desde que numero?: '))
        print(f'\n---Numeros de {n} hasta 1 \n')
        for x in range(n,0,-1):
            print(x,end=' ')
    else:
        print ('*****OPCION INVALIDA*****')

    res = input('\n\nDeseas continuar (S/N) ? ').upper()
    if res=='N':
     break
 
print('***Gracias por utilizar este programa***')