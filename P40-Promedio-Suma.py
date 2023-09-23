#Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0,
#además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse hasta que el usuario lo
#decida.


cc = n = suma = prom= 0
num=0

import os
os.system('cls')
while (True):
    print('\n ----Promedio y Suma de numeros----\n')
   
    while (num >= 0):
        num = int(input('Introduce el numero (usa "0" para finalizar la lista):  '))
        if num != 0:
            cc += 1
            suma += num
            prom = suma /cc
        else:
            break

    print ('\n\n+++++++++++++++Resultados++++++++++++++')
    print(f'\n-Se introdujeron {cc} numeros')
    print('\n-La suma de los numeros es:',suma)
    print(f'\n-El promedio de los numeros es: {prom:.2f}')
        
    res=input('\n ¿Deseas hacer otra lista de numeros(S/N)? ')
    
    if res.upper()=='N':
        break   
  
print("\n\n***Fin del Proceso****")
        

