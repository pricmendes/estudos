import random

from Pilha import Pilha

class inicializaPilha:
	def __init__(self):
		self.pilha = Pilha()
		self.menu()

	def imprimirPilha(self):
		print("\n Imprimindo conteúdo da pilha\n")
		print(self.pilha)

	def removerElementos(self):
		self.pilha.desempilha()
		print("Elemento removido")

	def incluirElemento(self):
		valor = input("Informe o valor a ser incluído\n")
		self.pilha.empilha(valor)
		print("Elemento incluido\n") # retirado um \n

	def incluirDezMilElementos(self):
		for i in range(10):
		    self.pilha.empilha(random.randint(1, 10000))

	def verificarPilhaEstaVazia(self):
		if self.pilha.vazio():
			print("Estrutura está vazia")
		else:
			print("Estrutura não está vazia")

	def menu(self):
		while True:
			opcao = input("1 - Incluir elemento na pilha\n"
						  "2 - Retirar elemento da pilha\n"
						  "3 - Exibir os elementos da pilha\n"
						  "4 - Incluir vários elementos na pilha\n"
						  "0 - Deseja sair?\n")
			if opcao =="1":
				self.incluirElemento()
			elif opcao == "2":
				self.removerElementos()
			elif opcao == "3":
				self.imprimirPilha()
			elif opcao == "4":
				self.incluirDezMilElementos()
			elif(opcao == "0"):
				break
			else:
				print("Opção inválida\n\n")

inicializaPilha = inicializaPilha()
