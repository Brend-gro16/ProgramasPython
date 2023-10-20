#Se desea procesar el pedido de una pizza en base a sus ingredientes, cada ingrediente tiene un precio, de acuerdo
#con lo siguiente
#• T – 1.50 (Tomate)
#• P – 3.50 (Peperoni)
#• A – 0.40 (Aguacate)
#• Q – 3.74 (Queso)
#• I – 2.10 (Piña)
#El usuario al pedir su pizza, pondrá las letras de los ingredientes que quiere, y el programa sumará el ingrediente las
#veces que aparezca, TT sumará 2 veces Tomate , TPQI, quiere Tomate, Peperoni, Queso y Piña.
#Consideraciones:
#• Se deberá calcular el total del pedido, sumando el precio de cada ingrediente.
#• El precio base es de 15 que se sumará al precio de los ingredientes elegidos.
#• Si el precio excede los 30, se aplicará un 5% de descuento.
#• Si no selecciona ingredientes, se le deberá mostrar un listado con los posibles ingredientes.
#• Si elije algún ingrediente erróneo, aunque haya alguno valido, mandar mensaje de error
#Notas: Puedes crear un diccionario para almacenar los ingredientes, la letra es la llave, el precio es el valor

import os
os.system('cls')

print('----------Segundo Examen Parcial----------\n\n')

ingredientes={'T':1.5,'P':3.5,'A':0.40,'Q':3.74,'I':2.10}





subtotal = 0
total=0
base=15
des=0


while (True):
    import os
    os.system('cls')
    subtotal = 0
    total=0
    base=15
    des=0


    print('\n\n**********PIZZERIA**********\n\n')
    print('Precio Base : 15')
    print('\n\nTomando su pedido...\n\nElija los ingredientes que desea de la siguiente lista: ("Enter" para continuar)')
    print('\n[T] Tomate\n[P] Peperoni\n[A] Aguacate\n[Q] Queso\n[I]Piña')
    pedido = input('\nIngredientes: ').upper()

    for i in pedido:
        if i in 'TPAQI':
            subtotal = subtotal + ingredientes[i]
        else:
            if i != 'TPAQI':
                print('\n******Error-Hay un elemento no valido-******\n******Solo se procesaran los elementos validos******')

                            
    subtotal = subtotal + base

    if subtotal <30:
        total = subtotal

    if subtotal >30 :
        print('\n--Has ganado un descuento de 5%--')
        des=subtotal*0.05
        total = subtotal-des

    if subtotal>15:
        print('\n\n-----------------------------------')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Descuento: {des:.2f}')
        print('-----------------------------------')
        print(f'\n*********Total: {total:.2f} *****') 
    else:
        print ('Error en la seleccion de ingredientes')
    res=input('\n ¿Deseas hacer otro pedido(S/N)? ')
    if res.upper()=='N': break   
    
print("\n\n****Fin del Proceso*****")
            





            
            
