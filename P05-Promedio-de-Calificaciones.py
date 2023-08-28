#Calcular el promedio de calificaciones


print('--Calculando el promedio de 3 calificaciones-- \n')
print('Dame 3 calificaciones separadas por un espacio')

c1, c2, c3 = input  ().split () #split divide la cadena en cada espacio
c1, c2, c3 = [float(c1), float (c2), float (c3)] 

suma = (c1 + c2 + c3 )
prom = suma /3

print(f'Las calificaiones son {c1},{c2},{c3}, la suma es {suma:.2f} y el promedio es {prom:.2f} ')