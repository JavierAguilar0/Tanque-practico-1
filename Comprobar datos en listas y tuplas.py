# Capítulo 24:Comprobar datos en listas y tuplas.
# Ejercicio 41
colores=('negro','azul','morado','rojo')
dato=input('escribe un color: ')
if dato in colores[0]:
	print('El color negro está admitido')
elif dato in colores[1]:
	print('El color azul está admitido')
elif dato in colores[2]:
	print('El color morado está admitido')
elif dato in colores[3]:
	print('El color rojo está admitido')
else:
	print('Color no admitido')