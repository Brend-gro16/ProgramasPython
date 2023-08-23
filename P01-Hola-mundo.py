#Lee datos y envia un saludo

print('\nLeyendo datos y enviando un saludo:\n')

nombre = input('Dame tu nombre: ') #Lee la cadena
edad = int(input('Dame la edad: ')) #Lee la cadena y convierte a entero
peso = float(input('Dame tu peso: ')) #Lee la cadena y convierte a flotante

print(f'\n --- {nombre} bienvenido a Python, tu edad es {edad}, tu peso es {peso}---\n ')
print(type(nombre))
print(type(edad))
print(type(peso))
