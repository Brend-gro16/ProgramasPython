# Conversión de grados Centigrados a grados  Farenheit

print('\n---Convertir de grados centigrados a farenheit --- ')

opcion = ( input('\n\n Elige una letra: \n Convertir a [C]entigrados o convertir a [F]ahrenheit: ') )

opcion = str.upper (opcion )

if opcion == 'C':
    
    print("\n\n-------Convirtiendo a Centigrados-------")
    T = float(input('\n Grados Fahrenhit: '))
    f = (T - 32) * 5 / 9
    print(f'\n\n *** {T} grados Fahrenheit = a {f:.2f} grados Centigrados***')
    
else :
    print('\n\n-------Conviritiendo a Farenheit-------')
    T = float (input('\n Grados Centigrados: '))
    f = ( T * 9 / 5 ) + 32
    print(f'*** {T} grados Fahrenheit = {f:.2} grados Centigrados***')
    
print ('\n\n                 Fin del proceso')