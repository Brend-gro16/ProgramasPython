#Calcula la paga de un trabajador, las  horas extra se pagan al doble

print('\n\n ---Calcula la paga de un trabajador, las  horas extra se pagan al doble---')

nombre = input('Nombre: ')
horas = int(input('Horas trabajadas: '))
paga = int(input('Paga x hora: '))

extra = 0

if horas > 40 :
    extra = horas - 40
    total = (40 * paga ) + ( (2 * paga) * extra  )
    
else :
    total = horas * paga
    
print(f'\n\n--{nombre} trabajo {horas} horas, con una paga de {paga}, {extra} horas extra\n pago total {total}')
