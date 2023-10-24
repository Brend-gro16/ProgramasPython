#Diseña un programa con una función que pida un número entero entre 1 y 7 y devuelva el día de la semana con
#letra.


import os
os.system('cls')

print('----------Dia de la Semana---------\n\n')

def dia(n):
    est=""
    if n==2:
        est="Lunes"
    elif n==3:
        est="Martes"
    elif n==4:
        est="Miercoles"
    elif n==5:
        est="Jueves"
    elif n==6:
        est="Viernes"
    elif n==7:
        est="Sabado"
    elif n==1:
        est="Domingo"
    else:
        est="Error"
    return est

n=int(input("Dame el numero de dia (1-7): "))
print(f"El dia de la semana es: {dia(n)}")
