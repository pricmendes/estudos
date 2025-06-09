import random

from Pilha import Pilha

class InicializaPilha:
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
        print("Elemento incluído\n")

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
            if opcao == "1":
                self.incluirElemento()
            elif opcao == "2":
                self.removerElementos()  # LIFO, último a entrar é o primeiro a sair
            elif opcao == "3":
                self.imprimirPilha()
            elif opcao == "4":
                self.incluirDezMilElementos()
            elif opcao == "0":
                break
            else:
                print("Opção inválida\n\n")

inicializaPilha = InicializaPilha()

# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 1
# saída print: Informe o valor a ser incluído
# saída print: 200
# saída print: Elemento incluído
# saída print: 
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 1
# saída print: Informe o valor a ser incluído
# saída print: 333
# saída print: Elemento incluído
# saída print: 
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 1
# saída print: Informe o valor a ser incluído
# saída print: 556
# saída print: Elemento incluído
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
# saída print: 0               2               556                 
# saída print: 1               1               333                 
# saída print: 2               0               200                 
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
# saída print: 3
# saída print: 
# saída print:  Imprimindo conteúdo da pilha
# saída print: 
# saída print: 
# saída print: Índice Lógico   Índice Real     Elemento            
# saída print: 0               12              1333                
# saída print: 1               11              4277                
# saída print: 2               10              5608                
# saída print: 3               9               4354                
# saída print: 4               8               8762                
# saída print: 5               7               1241                
# saída print: 6               6               4599                
# saída print: 7               5               804                 
# saída print: 8               4               3124                
# saída print: 9               3               8810                
# saída print: 10              2               556                 
# saída print: 11              1               333                 
# saída print: 12              0               200                 
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
# saída print: 0               11              4277                
# saída print: 1               10              5608                
# saída print: 2               9               4354                
# saída print: 3               8               8762                
# saída print: 4               7               1241                
# saída print: 5               6               4599                
# saída print: 6               5               804                 
# saída print: 7               4               3124                
# saída print: 8               3               8810                
# saída print: 9               2               556                 
# saída print: 10              1               333                 
# saída print: 11              0               200                 
# saída print: 
# saída print: 1 - Incluir elemento na pilha
# saída print: 2 - Retirar elemento da pilha
# saída print: 3 - Exibir os elementos da pilha
# saída print: 4 - Incluir vários elementos na pilha
# saída print: 0 - Deseja sair?
# saída print: 0