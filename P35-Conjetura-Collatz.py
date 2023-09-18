# Calcula la conjetura de Collatz


import os




while (True):
    os.system('cls')  
    
    while (True):
     print('---Calcula la conjetura de Collatz\n\n')
     num = int(input('Dame un entero positivo: '))      
     if num > 0: break
     
    while(num != 1): # Al llegar a 1 salir
        print(num,end=' ')
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
            
    print(num,end=' ')
    
    res= input('Deseas continuar (S/N)?')
    if res == 'N':
        break

print ('\n ****Proceso terminado****')