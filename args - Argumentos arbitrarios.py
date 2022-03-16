# Capítulo 35:*args - Argumentos arbitrarios.
# Ejercicio 52
def colores(*args):
	pass
colores('rojo', 'azul', 'verde', 'amarillo')#4
colores('lila', 'negro', 'rojo')#3
colores('rosa')#1
colores('marrón', 'naranja')#2
# Ejercicio 53
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
colores('Rojo','Negro')
# Ejercicio 54
def suma(*args):
    suma=args[0]+args[1]+args[2]+args[3]+args[4]
    print("El resultado de la suma es: ",suma)
suma(15,21,16,22,17)