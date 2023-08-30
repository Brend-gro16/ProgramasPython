# Verificar la suma de dos numeros, si  es = a un tercero

print('\n\n ---Verificar si la suma de dos numeros es igual a un tercero---')

print('\n Introduce 3 numeros enteros: ')

n1, n2, n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3 :
    
    print('\n ***La suma de n1 + n2 SI es =  n3 ***')
    
else :
    print('\n ***La suma de n1 + n2  NO ES =  n3 ***')
    