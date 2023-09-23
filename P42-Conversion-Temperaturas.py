#Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores
#introducidos por el usuario, es decir el usuario introduce la temperatura inicial y la temperatura final en grados
#centígrados y el programa realiza la conversión a farenheit incrementando el valor inicial en 1, hasta llegar al valor
#final. El proceso debe poder repetirse hasta que el usuario lo decida.

import os



while (True): 
    
    os.system('cls')
    print('\n ----Conversion de Celsius a Farenheit----\n')
    num1 = int(input('\n Grados Centigrados iniciales:  '))
    num2 = int(input('\n Grados Centigrados finales:  '))
    print ('\n\nCelsius\t Farenheit')    
    num2+=1

    while (num1 <= num2):
        if num1 < num2:
            f = ( num1 * 9 / 5 ) + 32
            print(f'  {num1}\t  {f:.2f}')
            num1 += 1        
    res=input('\n ¿Deseas hacer otra lista de numeros(S/N)? ')
    if res.upper()=='N': break   
    
print("\n\n***Fin del Proceso****")
            