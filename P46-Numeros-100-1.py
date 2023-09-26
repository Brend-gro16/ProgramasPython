# Numeros de 100 a 1 con for

print('\n\n----Numeros del 100 al x-----\n')

x = int(input('¿Desde que numero?: '))
y = int(input('\n¿De cuanto en cuanto desciende?:'))

for n in range(x,0,-y):
     print(n,end=' ') 