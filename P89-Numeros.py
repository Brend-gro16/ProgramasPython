#• Dados los siguientes números:
#◦ 50,60,70,80,90,100,200
#◦ 60,90,100,300,400,500
#◦ 10,20,60,90,70,100,600,700
#• Crear tres conjuntos, uno por cada lista de números y mostrarlos ( A, B, C)
#• Calcula y muestra:
#◦ unión de los conjuntos A y B ( A | B )
#◦ unión de los conjuntos B y C ( B | C )
#◦ diferencia de A y C ( A – C)
#◦ diferencia simétrica de B y C ( B ^ C)
#◦ intersección de B y C ( B & C )
#• Calcula y responda a las siguientes preguntas>
#◦ A es subconjunto de B ?
#◦ C es subconjunto de A ?
#◦ 100 esta en A ?
#◦ 60 esta en A , y en B y en C ?
#◦ 900 no esta en C ?

import os; os.system('cls')


print('----------Repaso de  Conjuntos\n\n')


A={50,60,70,80,90,100,200}
B={60,90,100,300,400,500}
C={10,20,60,90,70,100,600,700}

print(f'A= {A}')
print(f'B= {B}')
print(f'C= {C}')

print('\n\n--Union--')
print('A union con B', A|B)
print('B union con C', B|C)

print('\n\n---Diferencia---')
print('A Diferencia C', A-C)
print('\n\n---Diferencia Simetrica---')
print('B Diferencia Simetrica C',B ^ C)

print('\n\n---Interseccion---')
print('B Inteseccion C',B & C)

print ('\n-----Verificar si-----')
print('¿A es subconjunto de B?',A <= B)
print('¿C es subconjunto de A?',C <= A)
print('¿El numero 100 esta en A?:', 100 in A)
print('¿El numero 60 esta en  A?:', 60 in A)
print('¿El numero 60 esta en  B?:', 60 in B)
print('¿El numero 60 esta en  C?:', 60 in C)
print('¿El numero 900  NO esta en  C?:', 900 is not C)







