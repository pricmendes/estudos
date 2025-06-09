from collections import deque
from typing import Deque


class Fila(object): # Fila FIFO (primeiro a entrar é o primeiro a sair)
	# Inicializa os atributos
	def __init__(self):
		# Deque define o tipo de coleção da fila, está notado que irá receber apenas elemento do tipo "int"
		self.elementos: Deque[int]
		# Inicializa o objeto da coleção de fila
		self.elementos = deque()

	def incluirNaFila(self, elemento):
		# Inclui os elementos na fila
		self.elementos.append(elemento)

	# Método criado para facilitar a inclusão de vários elementos
	def incluirMuitosNaFila(self, variosElementos: list):
		for elemento in variosElementos:
			self.elementos.append(elemento)

	def retirarDaFila(self):
		# Retira um elemento da fila
		return self.elementos.popleft()

	# Reescrevendo o método para recuperar a quantidade de elementos
	def __len__(self):
		return len(self.elementos)

	# Reescrevendo o método para retornar o objeto como caracteres
	def __str__(self):
		retorno: str = "\n"
		for elemento in self.elementos:
			indice = self.elementos.index(elemento)
			retorno += str(indice) + " - " + str(elemento)
			retorno += "\n"

		return retorno
