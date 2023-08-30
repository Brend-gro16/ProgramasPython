# Calcular el tercer angulo de un triangulo

print ('--Calculado el tercer angulo de un triangulo-- \n\n ')
 
A1 = float (input('Escribe el primer angulo (grados) : '))
A2 = float (input('Escribe el segundo angulo (grados): '))

A3 = 180 - ( A1 + A2)

print (f'\n ---El tercer angulo mide: {A3} grados---')