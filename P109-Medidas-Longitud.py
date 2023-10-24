#Diseña un programa con dos funciones que convierta: pulgadas a centímetros y metros a pies. Deberá́ mostrar un
#menú con las opciones correspondientes.
#Considere las siguientes formulas:
# -centímetros = pulgadas * 2.54
# -pies = metros * 3.281

import os
os.system('cls')

print('----------Medidas de Longitud---------\n\n')

def centimetros(p):
    return(p*2.54)

def pies(m):
    return(m*3.281)

print("[ C ]entimetros")
print("[ P ]ies")

op=input("\nElije: ").upper()

if op=="C":
    p=int(input("Ingresa las Pulgadas: "))
    print(f"\n---Los centimetros  son: {centimetros(p)}---")
elif op=="P":
    m=int(input("Ingresa los metros: "))
    print(f"\n---Los pies son: {pies(m)}---")
else:
    print("\nOpcion incorrecta")