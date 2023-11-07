#Crear una clase

import os
import math
os.system('cls')

print('-----------Circulos ---------\n\n')

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def obtenerArea(self):
        return math.pi * math.pow(self.radio,2)
    
    def obtenerCircunferencia(self):
        return 2 * math.pi * self.radio
    
    def __str__(self):
        return f"Radio= {self.radio:.2f}, Area= {self.obtenerArea():.2f}, Circunferencia= {self.obtenerCircunferencia ():.2f}"
    
    
    
# Programa princial

circulo1 = Circulo(10.40)
print ('\n-------------Circulo 1 ------------')
print (circulo1)
print (f"El radio es: {circulo1.radio:.2f}")
print (f"El area es : {circulo1.obtenerArea ():.2f}")
print (f"La circunferencia es: {circulo1.obtenerCircunferencia():.2f}")

circulo2 = Circulo(12.45)
print ('\n-------------Circulo 2 -------------')
print(circulo2)
print (f"El radio es: {circulo2.radio:.2f}")
print (f"El area es: {circulo2.obtenerArea():.2f}")
print (f"La circunferencia es: {circulo2.obtenerCircunferencia():.2f}")

circulo3 = Circulo(100)
print ('\n-------------Circulo 3 -------------')
print(circulo3)
print (f"El radio es: {circulo3.radio:.2f}")
print (f"El area es: {circulo3.obtenerArea():.2f}")
print (f"La circunferencia es: {circulo3.obtenerCircunferencia():.2f}")

areaT= circulo1.obtenerArea() + circulo2.obtenerArea() + circulo3.obtenerArea()

print(f"\nEl area total es: {areaT:.2f}")
