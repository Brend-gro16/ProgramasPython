#Convierte de grados Centigrados a Fareheit y viceversa


import os
os.system('cls')

print('----------Conversion de Grados---------\n\n')

def faranheit(temp):
    return(temp*(9/5))+32

def centigrados(temp):
    return(temp-32)*(5/9)

#Programa principal
print("[ F ]arenhei")
print("[ C ]entrigrados")

op=input("\nElije: ").upper()


if op=="F":
    temp=int(input("Grados centigrados: "))
    print(f"\n---Los grados Farenheit son: {faranheit(temp)}---")
elif op=="C":
    temp=int(input("Grados Farenheit: "))
    print(f"\n---Los grados centigrados son: {centigrados(temp)}---")
else:
    print("\nOpcion incorrecta")
