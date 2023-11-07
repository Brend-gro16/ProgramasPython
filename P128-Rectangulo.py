#Crear una clase

import os
os.system('cls')

print('******************** Rectangulos ********************\n')

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho 
    def obtenerArea(self):
        return self.largo * self.ancho

    def obtenerPerimetro(self):
        return 2*self.largo + 2*self.ancho

    def __str__(self):
        return f'Largo = {self.largo}\nAncho = {self.ancho}\nArea = {self.obtenerArea():.2f}\nPerimetro = {self.obtenerPerimetro():.2f}'

# Programa principal

r1 = Rectangulo(12,3.4)
print ('\n-------------Rectangulo 1 ------------')
print(r1)

print (f"El area es : {r1.obtenerArea():.2f}")
print(f'El Perímetro es : {r1.obtenerPerimetro():.2f}')

r2 = Rectangulo(5.6,7.8)
print ('\n-------------Rectangulo 2 ------------')
print(r2)
print (f"El area es : {r2.obtenerArea ():.2f}")
print(f'El Perímetro es: {r2.obtenerPerimetro():.2f}')

rectangulos = []
rectangulos.append(r1)
rectangulos.append(r2)
print(rectangulos)