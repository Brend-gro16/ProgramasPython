#Una clase llamada Articulo la cual modela un artículo, con id, descripción, cantidad y precio, se describe
#en el siguiente diagrama de clase:
#---------------------------------------------------
#                     Articulo
#---------------------------------------------------
#- id
#- descripcion
#- cantidad
#- precio
#---------------------------------------------------
#+ __init__(self,id,descripcion,cantidad,precio)
#+ obtenerTotal(self)
#+ __str()__(self)
#----------------------------------------------------
#Tiene tres métodos: __init__() que es el constructor de la clase, obteneTotal() para calcular el total multi-
#plicando precio por cantidad, y __str__() para regresar los valores de los atributos de la clase.

#Cree la clase en Python que implemente el diseño anterior.


import os
os.system('cls')

print('\n\n******************** Articulos ********************\n')

class Articulo:
    def __init__(self, ID, descripcion, cantidad, precio):
        self.ID = ID
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio 
        
    def obtenerTotal(self):
        return self.cantidad * self.precio
    
    def __str__(self):
        return f"ID: {self.ID}, descripcion: {self.descripcion}, cantidad:  {self.cantidad}, precio: {self.precio}, Total: {self.obtenerTotal()}"


#El programa principal, deberá hacer uso de la clase creada de la siguiente forma:

# Programa principal
print ('\n               -------------Articulo 1 -------------')

art1 = Articulo('A101', 'Pluma Roja', 888, 0.08)
print(art1)

art1.cantidad = 999
art1.precio = 0.99

print ('\n')
print("Id = ",art1.ID)
print("Descripcion = ",art1.descripcion)
print("Cantidad = ",art1.cantidad)
print("Precio = ",art1.precio)
print("Total = ",art1.obtenerTotal())
print('-------------------------------------------------------------------')


print ('\n              -------------Articulo 2 -------------')
art2 = Articulo("A102", "Pluma Azul", 934, 1.2)
print(art2)
print('-------------------------------------------------------------------')


print ('\n\n           -------------Articulo 3 -------------')
art3 = Articulo("P103", "Lapiz del 12", 456, 0.5)
print(art3)
print('-------------------------------------------------------------------')


total = art1.obtenerTotal() + art2.obtenerTotal() + art3.obtenerTotal()
print('\n\n*************Total todos:', total,'*************')