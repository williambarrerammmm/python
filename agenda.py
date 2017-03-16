import amigo

class agenda:
	def __init__(self,dueño):
		self.dueño=dueño                   
		
	def agregarAmigo(self,amigos):
		self.dueño.append(amigos)
		
	def imprimirAmigos(self):
		print(self.amigos)
