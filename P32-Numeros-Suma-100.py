#Va sumando hasta que la suma llega a 100, aunque el ciclo establece llegar hasta
#200, evidentemente termina antes.

import os

os.system ('cls')

print ('------Imprimiendo numeros del "1" hasta alcanzar la suma de "n"')

c = 0
s = 0
while c < 200 :
    c += 1
    s += c
    print(c,end=" ")
    if s >= 1500 : # n = 1500
     print("\n")
     break

print(f"Hemos alcanzado el limite {s}, sumando {c} números")
