#Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: Tipo
#de usuario, paquete y cantidad.

#• Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500
#• Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900

#Se debe calcular un subtotal de la venta sumando el precio del tipo de usuario más el precio de tipo de paquete,
#y multiplicando por la cantidad solicitada.
#Se otrgará un descuento siempre y cuando el subtotal sea mayor a 5,000 y de acuerdo a lo siguiente:

#• Es Alumno 20%
#• Es Trabajador y un 10%
#• Es Docente y un 5%

#Al final mostrar un resumen con los datos calculados de la venta.
#Al terminar de procesar las ventas mostrar el total de ventas del día 


while (True):
    
    sub = float
    sub=0
    total = float
    total =0

    import os

    os.system ('cls')


    print ('++++++  Universidad Patio SA de CV  +++++++')
    print ('\n\n\n----Sistema de Inscripción Congreso de Sistemas---')

    print ('\n\n--------------Tipo de Usuario---------------\n')
    print ('[1]Alumno--$100')
    print ('[2]Trabajador--$200    ')
    print ('[3]Docente--$500  ')

    op1= int(input('\n\tElige el tipo de usuario: '))

    print ('\n\n---------------Tipo de Paquete---------------\n')
    print ('[1]Solo Conferencias--$600 ')
    print ('[2]Con Eventos Sociales--$800   ')
    print ('[3]Con Kit de Acceso--$900 ')

    op2= int(input ('\n\tElige el tipo de paquete: '))
    can= int(input('\n ¿Que cantidad de boletos?: '))

    if op1 == 1 and op2 == 1:
        x = 700
        sub= x*can
        if sub >= 5000:
            total = sub * (80/100)
        elif sub < 5000:
            total=sub   
        print('\n--------------TOTAL------------------')
        print (f'\n\n [1]Alumno....[1]Solo Conferencias...{can} boletos')
        print(f'*****El precio total por es: {total}')
        
    if op1 == 1 and op2 == 2:
        x = 900
        sub= x*can
        if sub >= 5000:
            total = sub * (80/100)
        elif sub < 5000:
            total=sub   
        print('\n--------------TOTAL------------------')
        print (f'\n\n [1]Alumno....[2]Con Eventos Sociales...{can} boletos')    
        print(f'*****El precio total es: {total}')

    if op1 == 1 and op2 == 3:
        x = 1000
        sub= x*can
        if sub >= 5000:
            total = sub * (80/100)
        elif sub < 5000:
            total=sub   
        print('\n--------------TOTAL------------------')
        print (f'\n\n[1]Alumno....[3]Con Kit de Acceso...{can} boletos')
        print(f'\n\n *****El precio total es: {total}')
        
    #Trabajador

    if op1 == 2 and op2 == 1:
        x = 800
        sub= x*can
        if sub >= 5000:
            total = sub * (80/100)
        elif sub < 5000:
            total=sub   
        print('\n--------------TOTAL------------------')
        print (f'\n\n [2]Trabajador....[1]Solo Conferencias...{can} boletos')
        print(f'*****El precio total por es: {total}')
        
    if op1 == 2 and op2 == 2:
        x = 1000
        sub= x*can
        if sub >= 5000:
            total = sub * (80/100)
        elif sub < 5000:
            total=sub   
        print('\n--------------TOTAL------------------')
        print (f'\n\n [2]Trabajador....[2]Con Eventos Sociales...{can} boletos')    
        print(f'*****El precio total es: {total}')

    if op1 == 2 and op2 == 3:
        x = 1100
        sub= x*can
        if sub >= 5000:
            total = sub * (80/100)
        elif sub < 5000:
            total=sub   
        print('\n--------------TOTAL------------------')
        print (f'\n\n[2]Trabajador....[3]Con Kit de Acceso...{can} boletos')
        print(f'\n\n *****El precio total es: {total}')
        
    # Docente

    if op1 == 3 and op2 == 1:
        x = 1100
        sub= x*can
        if sub >= 5000:
            total = sub * (80/100)
        elif sub < 5000:
            total=sub   
        print('\n--------------TOTAL------------------')
        print (f'\n\n [3]Docente....[1]Solo Conferencias...{can} boletos')
        print(f'*****El precio total por es: {total}')
        
    if op1 == 3 and op2 == 2:
        x = 1300
        sub= x*can
        if sub >= 5000:
            total = sub * (80/100)
        elif sub < 5000:
            total=sub   
        print('\n--------------TOTAL------------------')     
        print (f'\n\n [3]Docente....[2]Con Eventos Sociales...{can} boletos')    
        print(f'*****El precio total es: {total}')

    if op1 == 3 and op2 == 3:
        x = 1400
        sub= x*can
        if sub >= 5000:
            total = sub * (80/100)
        elif sub < 5000:
            total=sub   
        print('\n--------------TOTAL------------------')
        print (f'\n\n[3]Docente....[3]Con Kit de Acceso...{can} boletos')
        print(f'\n\n *****El precio total es: {total}')
    
        
    res=input('\n ¿Deseas hacer otro pedido(S/N)? ')
    if res.upper()=='N':
        break   

print("\n\n***Fin del Proceso****")





    

