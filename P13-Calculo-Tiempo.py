#Calculando el equivalente en  tiempo 

print ('\n\n--Calcular el equivalente de horas a dias, minutos y segundos--')

horas = float (input('\nIntroduce las horas: '))

dias = horas / 24 
min = horas * 60
segundos = min * 60  

print (f'\n{horas} horas esquivalen a: ')
print (f'\n\n{dias:.3f} dias')
print (f'{min:.3f} minutos')
print (f'{segundos:.3f} segundos')