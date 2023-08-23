#Calcular el area de un triangulo

print('Calcular el area de un triangulo \n')
print('Dame la base y la altura separados por un Enter')

base, altura = float(input()), float(input())
area = base * altura /2

print(f'El triangulo de base {base} y altura {altura} tiene un area de {area}')
