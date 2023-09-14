#Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V,
#VI, VII, VIII, IX, X). Si el número no esta en el rango solicitado que mande un mensaje de error.

import os

os.system ('cls')

print ('---Correspondencia entre un numero y equivalencia en romano--- \n ')

numero = int(input('\n Introduce un numero (0-10): '))

if numero == 1:
    print (' \n--- I --- \n ')
elif numero == 2:
    print ('\n--- II --- \n ')
elif numero == 3:
    print ('\n--- III --- \n ')
elif numero == 4:
    print ('\n--- IV --- \n ')
elif numero == 5:
    print ('\n--- V --- \n ')
elif numero == 6:
    print ('\n--- VI --- \n ')
elif numero == 7:
    print ('\n--- VII --- \n ')
elif numero == 8:
    print ('\n--- VIII --- \n ')
elif numero == 9:
    print ('\n--- IX --- \n ')
elif numero == 10:
    print ('\n--- X --- \n ')
    
    
    
else:
    print('\n\n +++El numero introducido esta fuera del rango+++')
    
    
    
    

