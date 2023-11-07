#Crear una clase

import os
import math
os.system('cls')

print('-----------Clasees-Empleado1 ---------\n\n')



# Clase
class Empleado: #Clase 
    def __init__(self, nombre, edad,sexo,casado): # Metodo constructor  (__init__)recibe valores y los asigna/(misma instancia, propiedades(nombre,edad))
        self.nombre = nombre #Asignar a atributos de la clase
        self.edad = edad
        self.sexo= sexo
        self.casado=casado
    def __str__(self): #Otro metodo (__str__) regresa una cadena con valores de los atributos
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {"Mujer" if self.sexo=="M" else "Hombre"}, Casado: {"Casado" if self.casado== True else "No Casado"}'
                                                                  #If de corto circuitp
# Programa principal

emp1 = Empleado('Jose Diaz', 35, "H", True)#Instancia 
print('\nNombre: ', emp1.nombre)
print('Edad:', emp1.edad)
print('Sexo:',emp1.sexo)
print('Casado:',emp1.casado)
print(emp1)

emp2 = Empleado('Maria Lopez',22, "M", False) #Instancia 
print('\nNombre: ', emp2.nombre)
print('Edad:', emp2.edad)
print('Sexo:',emp2.sexo)
print('Casado:',emp2.casado)
print(emp2) #En una sola linea

emp3 = Empleado('Rosario Valenzuela',15, "M",True) #Instancia 
print('\nNombre: ', emp3.nombre)
print('Edad:', emp3.edad)
print('Sexo:',emp3.sexo)
print('Casado:',emp3.casado)
print(emp3)

emp4 = Empleado ('Juan Perez', 20 , "H", False)
print('\nNombre: ', emp4.nombre)
print('Edad:', emp4.edad)
print('Sexo:',emp4.sexo)
print('Casado:',emp4.casado)
print(emp4)

prom= (emp1.edad+emp2.edad+emp3.edad+emp4.edad)/4
print("\n--Promedio de las edades: ", prom)

print(f"\nLos nombres son: {emp1.nombre}, {emp2.nombre}, {emp3.nombre}")
print('\n---------------------------------------------------------------')

if (emp2.casado == False and emp4.casado == False  ):
    print(f'\n{emp2.nombre} se puede casar con {emp4.nombre}')
    
    
if (emp1.casado == True and emp3.casado == True  ):
    print(f'\n{emp1.nombre}  No se puede casar con {emp3.nombre}')