#Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n),
#además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse hasta que el
#usuario lo decida.


import os

while(True):
    os.system('cls')
    print ('\n\n---------Numeros impares Ascendentes---------\n')
    n = int(input('¿Hasta que numero quieres llegar?:  '))
    num=0
    sum=0
    while (num < n):
        num+=1
        if num%2 != 0:
            sum=sum+num
            print (num)
            
    print (f'----La suma de los numeros es {sum}----')   
    
    res=input('\n ¿Deseas hacer otra lista de numeros(S/N)? ')
    if res.upper()=='N': break   
    
print("\n\n***Fin del Proceso****")
        
         
    

         
               