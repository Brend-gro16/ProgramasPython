#Calcula la paga total de un trabajador

print('\n -Calcula la paga de un trabajador-\n')

nombre = input('Nombre: ')
horas = int (input('Horas trabajadas: '))
paga = float(input('Paga por hora: '))

tasa= 0.03

pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print('\n----Resumen de pagos---- \n')
print(f'{nombre}, trabajo {horas} horas, con una paga de {paga} MXN/Hr , impuesto de {tasa}% \n')
print(f'Paga bruta: {pagabruta}')
print(f'Impuesto  : {impuesto}')
print(f'Paga neta : {paganeta}')

