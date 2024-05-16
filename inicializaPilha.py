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
				self.removerElementos() # LIFO, último a entrar é o primeiro a sair

			elif opcao == "3":
				self.imprimirPilha()
			elif opcao == "4":
				self.incluirDezMilElementos()
			elif(opcao == "0"):
				break
			else:
				print("Opção inválida\n\n")

inicializaPilha = inicializaPilha()


# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 1
# saída print: Informe o valor a ser incluído
# saída print: teste
# saída print: Elemento incluido
# saída print: 
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 1
# saída print: Informe o valor a ser incluído
# saída print: 20
# saída print: Elemento incluido
# saída print: 
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 1
# saída print: Informe o valor a ser incluído
# saída print: abc123
# saída print: Elemento incluido
# saída print: 
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 3
# saída print: 
# saída print:  Imprimindo conteúdo da pilha
# saída print: 
# saída print: 
# saída print: Índice Lógico   Índice Real     Elemento            
# saída print: 0               2               abc123              
# saída print: 1               1               20                  
# saída print: 2               0               teste               
# saída print: 
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 2
# saída print: Elemento removido
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 3
# saída print: 
# saída print:  Imprimindo conteúdo da pilha
# saída print: 
# saída print: 
# saída print: Índice Lógico   Índice Real     Elemento            
# saída print: 0               1               20                  
# saída print: 1               0               teste               
# saída print: 
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 4
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 2
# saída print: Elemento removido
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 3
# saída print: 
# saída print:  Imprimindo conteúdo da pilha
# saída print: 
# saída print: 
# saída print: Índice Lógico   Índice Real     Elemento            
# saída print: 0               10              540                 
# saída print: 1               9               613                 
# saída print: 2               8               4605                
# saída print: 3               7               2457                
# saída print: 4               6               4626                
# saída print: 5               5               1458                
# saída print: 6               4               4545                
# saída print: 7               3               1274                
# saída print: 8               2               1611                
# saída print: 9               1               20                  
# saída print: 10              0               teste               
# saída print: 
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 0