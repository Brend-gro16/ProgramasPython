#Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir
#0. El proceso debe poder repetirse hasta que el usuario lo decida.



import os
os.system('cls')
while (True):
    print('\n ----Numero Mayor----\n')
   
    while (num >= 0):
        num = int(input('Introduce el numero (usa "0" para finalizar la lista):  '))
        if num != 0:
            c=0
            if num > c:
                c=num
            
        else:
            break

    print ('\n\n+++++++++++++++Resultados++++++++++++++')
    print(f'\n-El numero mayor  es: {c}')
        
    res=input('\n ¿Deseas hacer otra lista de numeros(S/N)? ')
    
    if res.upper()=='N':
        break   
  
print("\n\n***Fin del Proceso****")