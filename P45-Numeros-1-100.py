# Imprime los numeros del 1 al x

print('\n\n----Numeros del 1 al x-----\n')

x = int(input('¿Hasta que numero?: '))
y = int(input('\n¿De cuanto en cuanto?:'))
print('\n')
for n in range(1,x+1,y):
    
    print(n,end=' ')