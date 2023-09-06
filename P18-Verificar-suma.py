#Verifica si la suma de dos numeros es igual a un tercero

#459 594 945 333 667


import os

os.system ('cls')


print('----Verifica si la suma de dos numeros es igual a un tercero----')
print('\nDame 3 numeros enteros separados por un espacio')
n1, n2, n3 = input().split()

n1, n2, n3 = (int(n1),int(n2),int(n3))

if n1 + n2 == n3:
    print('n1 + n2 = n3')
elif n1 + n3 == n2:
    print ('n1 + n3 = n2')
elif n2 + n3 == n1:
    print ('n2 + n3 = n1 ')
elif n1 == n2 == n3:
    print ('--Los tres numeros son iguales--')
else:
    print('--Hay dos numeros iguales o todos son diferentes--')

print ('\n\n **Proceso terminado**' ) 