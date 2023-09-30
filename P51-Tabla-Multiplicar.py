# tabla de multiplicar con for

import os

while(True):
    os.system('cls')
    
    print('\n\n-----Tabla de multiplicar con for----- \n')
    t = int(input('Numero de tabla: '))
    n = int(input('¿Hasta que numero? '))
    print("\n")
    
    for i in range(1, n+1):
     print(f'{t} x {i} = {t*i}')

    res = input('\n\n¿Deseas continuar (S/N) ? ').upper()
    if res=='N':
         break

print('\n***Gracias por utilizar este programa***')