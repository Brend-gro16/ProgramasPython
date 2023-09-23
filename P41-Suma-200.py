#Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, luego mostrar
#cuantos números fueron introducidos y la suma de estos. El proceso debe poder repetirse hasta que el usuario lo
#decida.



import os


while (True):
    os.system('cls')
    print('\n ----Suma de numeros----\n')
    cc = n = suma = prom= 0
    num=0
   
    while (suma <= 200):
        num = int(input('Introduce el numero que quieres sumar:  '))
        suma += num
        cc += 1
        if suma >200:   
         print ('\n\n+++++++++++++++Resultados++++++++++++++')
         print(f'\n-Se introdujeron {cc} numeros')
         print('\n-La suma de los numeros es:',suma)
         
    res=input('\n ¿Deseas hacer otra lista de numeros(S/N)? ')
    if res.upper()=='N':
         break   

print("\n\n***Fin del Proceso****")
        

