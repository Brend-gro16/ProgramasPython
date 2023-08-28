# Dividir en cifras un numero entero

import math

print('--Dividir un numero entero en  unidades, decenas y centenas--\n\n')

numero = int(input('Dame un numero entero de 3 cifras: '))
                   
centenas = math.trunc( numero / 100 )
decenas = math.trunc( (numero - centenas * 100) / 10 )
unidades = numero - (centenas * 100 + decenas * 10)

print(f'Centenas:{centenas}\nDecenas:{decenas}\nUnidades:{unidades}')
print(f'Suma digitos:{centenas + decenas + unidades}')