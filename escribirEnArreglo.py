nombre=''
lista=[]
while(nombre != 'salir'):
	nombre=input('Ingrese el nombre del amigo: ')
	if(nombre  in lista):
		print('El amigo ya esta')
	if(nombre not in lista):
		lista.append(nombre)
print(lista)
