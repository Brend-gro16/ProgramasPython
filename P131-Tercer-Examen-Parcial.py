import os;os.system('cls')


print('***TERCER EXAMEN PARCIAL***')

class Jugador:
    def __init__(self, nombre, año, sexo,becado):
        self.nombre = nombre
        self.año = año
        self.sexo = sexo 
        self.becado=becado
    
    def __str__(self):
        return f'Nombre: {self.nombre},Año:  {self.año}, Sexo: {self.sexo}, Becado: {"Con Beca" if self.becado == True else "No Becado"}'
  
class Categoria:
    def __init__(self,nombre,rango,costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores= list()
        
    
    def agregarjugador(self,jugador):
        self.jugadores.append(jugador)
            
    def hombres(self):
        hombres = 0
        hombres = sum(1 for jugador in self.jugadores if jugador.sexo == 'Hombre' ) 
        return hombres
    def mujeres(self):
        mujeres = 0
        mujeres = sum(1 for jugador in self.jugadores if jugador.sexo == 'Mujer')
        return mujeres
    
    def subtotal(self):
        total = 0
        for jugador in self.jugadores:
            if not jugador.becado:
                total += self.costo
        return total
    def __str__(self):
        return f'Categorias -> [Nombre:{self.nombre}Rango:{self.rango}Costo:{self.costo}]'
    
class Academia:
    def __init__(self,nombre,propietario,domicilio,):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias=list()
    def agregarCategoria(self,categoria):
        self.categorias.append(categoria)  
    def __str__(self):
        return f'Academia -> [Nombre:{self.nombre}Propietario:{self.propietario}Domicilio:{self.domicilio}]'
    def total(self):
        total = 0
        for categoria in self.categorias:
            total += categoria.subtotal()
        return total
    


def main():

 print('\n\n******************** Academia********************\n')
print('\nInicio del programa principal en la funcion main ()')

#Categorias de la Academia
miacademia = Academia(nombre ='Academia Santos Laguna',propietario= 'Francisco Nava', domicilio= 'Aguanaval 123, Hidraulica')

miacademia.agregarCategoria( Categoria(nombre='Junior A',rango='2006/2007/2008',costo=1250.00))
miacademia.agregarCategoria( Categoria(nombre='Junior B',rango='2009/2010/2011',costo=850.00 ))
miacademia.agregarCategoria( Categoria(nombre='Pony A',rango='2012/2013/2014',costo=700.00) )


#Jugares de cada categoria
miacademia.categorias[0].agregarjugador(Jugador(nombre='Alexander Lopez ',año='2006',sexo='Hombre',becado= False))
miacademia.categorias[0].agregarjugador(Jugador(nombre='Uriel Puga',año='2007',sexo='Hombre',becado= True))
miacademia.categorias[0].agregarjugador(Jugador(nombre='Alejandra Escalona ',año='2008',sexo='Mujer',becado= False))

miacademia.categorias[1].agregarjugador(Jugador(nombre='Armando Santana',año='2009',sexo='Hombre',becado= False))
miacademia.categorias[1].agregarjugador(Jugador(nombre='Daniel Mijares',año='2010',sexo='Hombre',becado= False))
miacademia.categorias[1].agregarjugador(Jugador(nombre='Antonio Hernandez ',año='2011',sexo='Hombre',becado= True))


miacademia.categorias[2].agregarjugador(Jugador(nombre='Andrea Solis',año='2012',sexo='Mujer',becado= True))
miacademia.categorias[2].agregarjugador(Jugador(nombre='Marissa Hernandez',año='2013',sexo='Mujer',becado= True))
miacademia.categorias[2].agregarjugador(Jugador(nombre='Diana Soto',año='2014',sexo='Mujer',becado= True))

 
#Reporte

print (f'\nREPORTE DEL CLUB DEPORTIVO\n')
print("Nombre: ",miacademia.nombre)
print("Propietario: ",miacademia.propietario)
print("Domicilio: ",miacademia.domicilio)
print (f'\nTotal de categorias: {len(miacademia.categorias)} ')

#---------------------------------------------------------------
hombres=0
mujeres = 0    

for categoria in miacademia.categorias:
        for jugador in categoria.jugadores:
            if jugador.sexo == 'Hombre':
                hombres += 1
            elif jugador.sexo == 'Mujer':
                 mujeres += 1
                 
print (f'Total de Hombres : {hombres}')
print (f'Total de Mujeres: {mujeres}')
#---------------------------------------------------------------


print('\n>> Datos generales de las categorias\n')
for Categoria in miacademia.categorias:
        print(f'Nombre:{Categoria.nombre:<20}Rango: {Categoria.rango:<20}Costo: ${Categoria.costo:>10}')       
print('\n>> Jugadores por Categoria')   
       
for Categoria in miacademia.categorias:
    
    print(f'\n{Categoria.nombre} - {Categoria.rango} - ({len(miacademia.categorias)})')
    
    total=0
    total1 = categoria.subtotal()+total
    for Jugador in Categoria.jugadores:
            print(f'Nombre: {Jugador.nombre:23}AñoNac:{Jugador.año:<10}Sexo: {Jugador.sexo:<10}Becado: {Jugador.becado:<10}')
    print(f'\nSubtotal: ${categoria.subtotal():,.2f}\n')        
    


          
print(f'\n\n-> Total: {total1:,.2f}')
if __name__ == '__main__':
    main()