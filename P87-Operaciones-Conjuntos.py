#Nos permite ejemplificar las operaciones logicas sobre conjuntos

import os
os.system('cls')

print('\n\n-------Operaciones Sobre Conjuntos-------\n\n')

c1={1,2,3,4,5}
c2={5,6,7,8,9,10}
c3={9,10,11,12,13}
c4={3,4,5}

print(c1,c2,c3,c4)

print('\n\n--Union--')

print('C1 union con C3', c1.union(c2))
print('C1 union con C3', c1|c2)

print('\n\n---Interseccion---')
print('C1 Inteseccion C2',c1.intersection(c2))
print('C2 Inteseccion C3',c2 & c3)

print('\n\n---Diferencia---')
print('C1 Diferencia C2',c1.difference(c2))
print('C2 Diferencia C3',c2 - c3)


print('\n\n---Diferencia Simetrica---')
print('C1 Diferencia Simetrica C2',c1.symmetric_difference(c2))
print('C2 Diferencia Simetrica C3',c2 ^ c3)

print('\n\n---Comprobamos Subconjuntos---')
print('C4 es subconjunto de C1:', c4.issubset(c1))
print('C3 es subconjunto de C2:', c3<=c2)

##Igual que los subconjuntos preguntando al reves
print('\n\n---Comprobamos Superconjuntos---')
print('C1 es superconjunto de C4:', c1.issuperset(c4))
print('C2 es superconjunto de C3:', c2>=c3)

print('\n\n---Verificar---')
print('¿El numero 2 esta en  C1?:', 2 in c1)
print('¿El numero 6 no esta en C1?', 6 is not c1)








