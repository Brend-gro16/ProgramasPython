# Operaciones matematicas

x = float(input('Dame un numero "x": '))
y = float(input('Dame un numero "y": '))


suma = x+y
resta = x-y
mult = x*y
div = x/y
dive = x // y #division entera
res = x % y #residuo de la division 
exp = x ** y

print('\n --Operaciones matematicas-- \n')
print(f'-Suma:{suma}\n-Resta:{resta}\n-Multiplicacion:{mult}\n-Division:{div}')
print(f'-Division entera:{dive}\n-Residuo:{res}\n-Exponenciacion:{exp:.3f}\n')