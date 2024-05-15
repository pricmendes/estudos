class Pilha(object):
	# Inicializa a pilha
	def __init__(self):
		self.elementos = []

	# Método para fazer o empilhamento dos elementos
	def empilha(self, elemento):
		self.elementos.append(elemento)

	# Método para fazer o desempilhamento dos elementos
	def desempilha(self):
		return self.elementos.pop()

	# Método para verificar se a pilha está vazia
	def vazio(self):
		return len(self.elementos) == 0

	# Método sobreescrito para converter o objeto em caracteres
	def __str__(self):
		retorno: str = "\n{um} {dois} {tres}\n"\
			.format(um = "Índice Lógico".ljust(15), dois = "Índice Real".ljust(15), tres = "Elemento".ljust(20))

		contador = 0
		# Exibindo a pilha de forma inversa
		for elemento in self.elementos[::-1]:
			indice = self.elementos.index(elemento)
			retorno += "{um} {dois} {tres}"\
				.format(um = str(contador).ljust(15), dois = str(indice).ljust(15), tres = str(elemento).ljust(20))
			retorno += "\n"
			contador += 1

		return retorno