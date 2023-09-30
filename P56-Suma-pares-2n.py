#Se desea imprimir los pares de 2 a n y su suma
#Dame número: 20
#Salida: 2 4 6 8 10 12 14 16 18 20 , La suma es = xxx


import os
os.system('cls')

print('\n\n-----Suma de numeros pares (2 a n)-----')

num= int(input('\n Introduce un numero:  '))
suma=0
for i in range(0,num+1,2):
  
    print(f'{i}  ', end='')
    suma=suma+i
    
print(f'\n\n----La suma es {suma}----')

     

     


    