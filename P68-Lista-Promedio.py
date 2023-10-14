#Crear un programa que permita procesar una lista de n números enteros, de acuerdo a lo siguiente:
#• Leer n números por parte del usuario
#• Agregar cada número a la lista
#• Mostrar la lista
#• Iterar por la lista y sacar la suma de sus elementos
#• Calcular luego el promedio de los n


import os

os.system('cls')

print('-------------Procesando Calificaciones-------------\n\n')
print('-----Introduce las calificaciones 0-9 (11 para terminar):')

cal=[]
n=0
suma=0
promedio=0

while n<=10:
    n = float(input('Introduce la calificacion: '))
    if n!=11:
        cal.append(n)
        suma =suma+n
    
    elif n==11:
        break

promedio = suma/len(cal)

print (f'\n\nLa lista de calificaciones es: {cal}')
print(f'La suma de calificaciones es: {suma}\n')
print(f'-----El promedio de calificaciones es: {promedio:.2f}-----')

