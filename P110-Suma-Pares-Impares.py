#Diseña un programa con una función que reciba tres parámetros: dos números (un rango), una letra P o I y nos
#regrese la suma de números pares o impares en el rango de números especificados.
#El programa deberá́ mostrar un menú́ con las opciones correspondientes y llamara a la función según la opción
#seleccionada.

import os
os.system('cls')

print('----------Suma Pares Impares---------\n\n')

def suma(ini, fin, letra):
    s = 0
    if letra=='P':
        for i in range(ini, fin+1,2):
            if i%2==0:
                s += i       
    if letra=='I':
        for i in range(ini, fin+1,1):
            if i%2 !=0:
                s+=i
    return s   

print('-----Introduce el rango de numeros a sumar---- ')
ini=int(input('Inicio: '))
fin=int(input('Fin: '))
letra=(input('\n[P]ares\n[I]mpares\nElije la letra: ')).upper()
print('-'*35)
print(f'Suma del rango introducido: {suma(ini,fin,letra)}')
print('-'*35)