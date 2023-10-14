# Estudiante


import os; os.system('cls')
estudiante = {
    
'Nombre':'Juan Perez',
'Edad':'45',
'Email':'jperez@msn.com',
'Carrera':'Sistemas'
}
print(f'\nEl diccionario: \n{estudiante}')

estudiante['Calificacion']= '9.5'
estudiante['Email']='juanp@gmail.com'
print(f'\nEl diccionario actualizado: \n{estudiante}')


print('\n---Las llaves---')
for k in estudiante.keys():
    print(k, end = " ")
    
print('\n\n---Los valores---')
for v in estudiante.values():
    print(v, end = " ")

print("\n\n---Llaves y valores---")
for k,v in estudiante.items():
    print(f'{k:<12} : {v}')