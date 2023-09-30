#Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma:
#¿Cuántos términos?? 5
#Salida: 1 + 1/2! + 1/3! + 1/4! + 1/5! , suma: 2.283333333333333


import os
os.system('cls')

print('\n\n-----Imprime secuencia de terminos armonicos y su suma---- \n')

n = int(input('Numero de terminos: '))
print('   0')
suma=0

for i in range(1,n+1):
    
        suma= suma + (1/i)
        print(f'\n + 1/{i}!   ',end=" ")
        
print('\n___________')
print(f' {suma:.5f}',end='')

print(f'\n\n*****La Suma de terminos armonicos es {suma:.5}*****')