from fila import Fila

class InicializaFila:

    # Inicializa o atributo fila e executa o método de menu
    def __init__(self):
        self.fila: Fila = Fila()
        self.menu()

    # controla o menu de opções
    def menu(self):
        while True:
            opcao = input("1 - Incluir elemento na fila.\n"
                          "2 - Retirar elemento da fila.\n"
                          "3 - Exibir os elementos da fila.\n"
                          "4 - Incluir vários elementos na fila.\n"
                          "0 - Deseja sair?\n")
            if opcao == "1":
                self.incluir()
            elif opcao == "2":
                self.remover()
            elif opcao == "3":
                self.imprimir()
            elif opcao == "4":
                self.incluirVarios()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.\n\n")
    # Incluindo um único elemento
    def incluir(self):
        valor = int(input("Informe o valor inteiro a ser incluído:\n"))
        self.fila.incluirNaFila(valor)
        print("Elemento incluído:\n\n")

    # Remove um único elemento
    def remover(self):
        self.fila.retirarDaFila()
        print("Elemento removido:\n\n")

    # Imprime todos os elementos
    def imprimir(self):
        if self.fila.__len__() > 0:
            print("Os elementos atuais na fila são:\n", self.fila.__str__())
        else:
            print("Não existem elementos na fila.\n")

    # Inclui vários elementos
    def incluirVarios(self):
        quantidade = int(input("Informe a quantidade de elementos a serem incluídos:\n"))
        valores: list = []
        for i in range(quantidade):
            valor = int(input(f"Informe o valor {i + 1}\n"))
            valores.append(valor)
        self.fila.incluirMuitosNaFila(valores)
        print("Elementos incluídos:", valores, "\n\n")            

InicializaFila()


# Output: 1 - Incluir elemento na fila.
# Output: 2 - Retirar elemento da fila.
# Output: 3 - Exibir os elementos da fila.
# Output: 4 - Incluir vários elementos na fila.
# Output: 0 - Deseja sair?
# Output: 4
# Output: Informe a quantidade de elementos a serem incluídos:
# Output: 3
# Output: Informe o valor 1
# Output: 5
# Output: Informe o valor 2
# Output: 6
# Output: Informe o valor 3
# Output: 10
# Output: Elementos incluídos: [5, 6, 10] 
# Output: 
# Output: 
# Output: 1 - Incluir elemento na fila.
# Output: 2 - Retirar elemento da fila.
# Output: 3 - Exibir os elementos da fila.
# Output: 4 - Incluir vários elementos na fila.
# Output: 0 - Deseja sair?
# Output: 1
# Output: Informe o valor inteiro a ser incluído:
# Output: 32
# Output: Elemento incluído:
# Output: 
# Output: 
# Output: 1 - Incluir elemento na fila.
# Output: 2 - Retirar elemento da fila.
# Output: 3 - Exibir os elementos da fila.
# Output: 4 - Incluir vários elementos na fila.
# Output: 0 - Deseja sair?
# Output: 3
# Output: Os elementos atuais na fila são:
# Output:  
# Output: 0 - 5
# Output: 1 - 6
# Output: 2 - 10
# Output: 3 - 32
# Output: 
# Output: 1 - Incluir elemento na fila.
# Output: 2 - Retirar elemento da fila.
# Output: 3 - Exibir os elementos da fila.
# Output: 4 - Incluir vários elementos na fila.
# Output: 0 - Deseja sair?
# Output: 1
# Output: Informe o valor inteiro a ser incluído:
# Output: 16
# Output: Elemento incluído:
# Output: 
# Output: 
# Output: 1 - Incluir elemento na fila.
# Output: 2 - Retirar elemento da fila.
# Output: 3 - Exibir os elementos da fila.
# Output: 4 - Incluir vários elementos na fila.
# Output: 0 - Deseja sair?
# Output: 3
# Output: Os elementos atuais na fila são:
# Output:  
# Output: 0 - 5
# Output: 1 - 6
# Output: 2 - 10
# Output: 3 - 32
# Output: 4 - 16
# Output: 
# Output: 1 - Incluir elemento na fila.
# Output: 2 - Retirar elemento da fila.
# Output: 3 - Exibir os elementos da fila.
# Output: 4 - Incluir vários elementos na fila.
# Output: 0 - Deseja sair?
# Output: 2
# Output: Elemento removido:
# Output: 
# Output: 
# Output: 1 - Incluir elemento na fila.
# Output: 2 - Retirar elemento da fila.
# Output: 3 - Exibir os elementos da fila.
# Output: 4 - Incluir vários elementos na fila.
# Output: 0 - Deseja sair?
# Output: 3
# Output: Os elementos atuais na fila são:
# Output:  
# Output: 0 - 6
# Output: 1 - 10
# Output: 2 - 32
# Output: 3 - 16
# Output: 
# Output: 1 - Incluir elemento na fila.
# Output: 2 - Retirar elemento da fila.
# Output: 3 - Exibir os elementos da fila.
# Output: 4 - Incluir vários elementos na fila.
# Output: 0 - Deseja sair?
# Output: 0


