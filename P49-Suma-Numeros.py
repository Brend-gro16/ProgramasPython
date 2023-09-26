# Suma y promedio de numeros introducidos


print('\n-----Suma y promedio de n números introducidos por el usuario-----')

n = int(input('\n\n¿Cuantos numeros vas a sumar y promediar?: '))
suma = 0
prom=0

for c in range(1,n+1):
    num = float(input(f"Introduce el número {c}: "))
    suma += num
    prom=suma/n
 
print('\n\t----------RESULTADOS----------')    
print(f'\n--La suma es {suma}--')
print(f'\n--El promedio  es {prom}--')