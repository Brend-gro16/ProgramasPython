#Ventas

import os
os.system('cls')



class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio 
        self.total=cantidad*precio
    def __str__(self):
        return f"Articulo: {self.articulo},Cantidad:  {self.cantidad:>10.2f}, Precio: {self.precio:>10,.2f}, Total: {self.total:>10,.2f}"

class Cliente:
    def __init__(self, RFC,Nombre,Domicilio,Correo):
        self.RFC = RFC
        self.Nombre = Nombre
        self.Domicilio = Domicilio
        self.Correo = Correo
        self.ventas= list()
    def agregarVenta(self,venta):
        self.ventas.append(venta)
    def totalImporteVentas(self):
        total=0
        for venta in self.ventas:
            total+= venta.total
        return total
    def __str__(self):
        return f'Cliente-> [Nombre: {self.Nombre:<20} RFC: {self.RFC:<12} Domicilio: {self.Domicilio:<25}Correo: {self.Correo:<30}]'
    
class Tienda:
    def __init__(self,Nombre,Domicilio,Propietario):
        self.Nombre = Nombre
        self.Domicilio = Domicilio
        self.Propietario = Propietario
        self.clientes=list()
    def agregarCliente(self,cliente):
        self.clientes.append(cliente)
    def totalVentas(self):
        total=0
        for Cliente in self.clientes:
            total +=len(Cliente.ventas)
        return total
    def totalImporteVentas (self):
        total=0
        for Cliente in self.clientes:
            total+=Cliente.totalImporteVentas()
        return total
    def __str__(self):
        return f'Tienda -> [Nombre:{self.Nombre}Domicilio:{self.Domicilio}Propietario:{self.Propietario}]'
    

def main():
 import os
os.system('cls')
print('\n\n******************** Ventas ********************\n')
print('\nInicio del programa principal en la funcion main ()')

#Clientes de la Tienda
mitienda = Tienda(Nombre ='Ferreteria las Lomas',Domicilio= 'Av.Luis Moya 345', Propietario= 'Carlos Castaneda')
mitienda.agregarCliente( Cliente(RFC='JELI120240',Nombre='Felipe Calderon',Domicilio='Las Lomas 123',Correo='calde@msn.com') )
mitienda.agregarCliente( Cliente(RFC='PEÑA121250',Nombre='Enrique Peña',Domicilio='5 de Mayo 321',Correo='quique@gmail.com') )
mitienda.agregarCliente( Cliente(RFC='AMLO101145',Nombre='Andres Lopez',Domicilio='Palacio Nacional 321',Correo='peje@yahoo.com') )
mitienda.agregarCliente( Cliente(RFC='GELA666666',Nombre='Xochitl Gelatinas',Domicilio='Danone 123',Correo='xochitl@precidencia.gob.mx') )

#Ventas para Cada Cliente
mitienda.clientes[0].agregarVenta(Venta(articulo='Martillo',cantidad=10,precio=60.5))
mitienda.clientes[0].agregarVenta(Venta(articulo='Pala',cantidad=2,precio=1170.55))
mitienda.clientes[1].agregarVenta(Venta(articulo='Clavos',cantidad=2.5,precio=160.34))
mitienda.clientes[1].agregarVenta(Venta(articulo='Cinta de Aislar',cantidad=5,precio=71.34))
mitienda.clientes[2].agregarVenta(Venta(articulo='Tinner',cantidad=50,precio=65.00))
mitienda.clientes[3].agregarVenta(Venta(articulo='Pinzas de Chofer',cantidad=1,precio=300.00))


#Reporte
print (f'Reporte de ventas: {mitienda}')
print (f'Total de clientes: {len(mitienda.clientes)} ')
print (f'Total de Ventas : {mitienda.totalVentas()}')
print('\n---CLientes---')

for Cliente in mitienda.clientes:
        print(Cliente)
for Cliente in mitienda.clientes:
        print(f'\n{Cliente.RFC}----{Cliente.Nombre}----{Cliente.totalImporteVentas():,.2f}')
        for Venta in Cliente.ventas:
            print(f'{Venta}')
            
print(f'\n\nTotal importe Ventas: {mitienda.totalImporteVentas():,.2f}')
if __name__ == '__main__':
    main()