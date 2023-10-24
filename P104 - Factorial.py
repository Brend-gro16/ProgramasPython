#Calcula el factorial de un numero entero

import os
os.system('cls')

print('----------Factorial---------\n\n')

def factorial(n):
    f=1
    for n in range(1,n+1):
        f=f*n
    return f

#Programa principal
n=int(input("Numero: "))
print(f"El factorial de {n} es {factorial(n)}")