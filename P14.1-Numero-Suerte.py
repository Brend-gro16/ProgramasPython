# Numero de la suerte

print ('\n\n ---Calculando el numero de la suerte---\n')

año = input('Ingresa el año de nacimiento (4 digitos): ')

def sumar (cadena):
    suma = 0
    for i in cadena:
     if i.isdigit():
            suma += int(i)

    return suma


print(f'\n****El numero de la suerte es: {sumar(año)}****') 