#Dados los siguientes nombres:
#• Juan, Maria, Pedro, Jose, Rocio
#• Pedro, Juan, Pablo, Mateo, Esther
# Crea dos conjuntos uno para cada lista de nombres y muéstralos ( A, B )
# Calcula y muestra:
#◦ union de los conjuntos ( A | B)
#◦ intesección de los conjuntos ( A & B)
#◦ diferencia de los conjuntos ( A – B )
#◦ diferencia simetrica de los conjuntos ( A ^ B )
#Calcula y muestra también
#◦ si el conjunto de nombres Pablo, Mateo, es subconjunto de B
#◦ si el conjunto A, es superconjunto del conjunto de nombres: Reynaldo, Angelica
#◦ si Pedro esta en A
#◦ si Lilia no esta en B

import os; os.system('cls')


print('----------Repaso de  Conjuntos\n\n')


A= {'Juan', 'Maria', 'Pedro', 'Jose','Rocio'}
B= {'Pedro', 'Juan', 'Pablo', 'Mateo','Esther'}

print(f'A={A}')
print(f'B={B}')

print('\n\n--Union--')
print('A union con B', A.union(B))#A|B)

print('\n\n---Interseccion---')
print('A Inteseccion B',A.intersection(B))#A&B

print('\n\n---Diferencia---')
print('A Diferencia B',A.difference(B))#A-B

print('\n\n---Diferencia Simetrica---')
print('A Diferencia Simetrica B',A.symmetric_difference(B))#A^B


print('\n\n---Comprobar Subconjunto(Pablo Mateo) en B---')
C= {'Pablo','Mateo'}
print (f'C={C}')
print('C es subconjunto de B:', C.issubset(B))#C<=B

print('\n\n---Comprobar  si A es Superconjunto de D  ---')
D={'Reynaldo','Angelica'}
print(f'D= {D}')
print('A es superconjunto de D:', A.issuperset(D))


print('\n\n---Verificar si ---')
print('¿Pedro esta en A?:', 'Pedro' in A)
print('¿Lilia no esta en B?', 'Lilia' is not B)






