# Tabla de conversion de Peso a Dollar

import os
tc = 19.13 ; tcl=22.22



while(True):
    os.system('cls')
    
    while (True):
        print ('****Conversion Peso - Dollar*****\n\n')
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final : "))
        if (pi < pf):
         break
    c=pi
    print("\nPesos\tDollar")
    print("-"*15)
    while c<=pf :
    
        print(f'{c}\t{c/tc:.2f}')
        c+=1
        print("-"*15)
    res=input('\nDeseas Continuar(S/N)? ').upper()
    if res =='N':
        break
        

print ('\n ****Proceso terminado****')