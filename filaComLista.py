class filaComLista(object):
	# Inicializa os atributos
    def __init__(self):
        self.elementos = []
        
	# Inclui os elementos na fila
    def incluirNaFila(self, elemento):
        posicao = self.elementos.__len__()
        self.elementos.insert(posicao, elemento)
        
	# Retira o elemento da fila
    def retirarDaFila(self):
        listaAuxiliar = self.elementos.copy()
        self.elementos = []
        for i in range(listaAuxiliar.__len__()):
            if i != 0: # se diferente de 0
                self.elementos.append(listaAuxiliar[i])
                
	# Reescrevendo o método para recuperar a quantidade de elementos
    def __len__(self):
        return len(self.elementos) #return
    
	# Reescrevendo o método para retornar o objeto como caracteres
    def __str__(self):
        retorno: str = "\n"
        for elemento in self.elementos:
            indice = self.elementos.index(elemento)
            retorno += str(indice) + " - " + str(elemento)
            retorno += "\n"
        return retorno

filaComLista = filaComLista()
filaComLista.incluirNaFila(10)
filaComLista.incluirNaFila(23)
filaComLista.incluirNaFila(143)
print(filaComLista.__str__())
filaComLista.retirarDaFila() # FIFO, primeiro a entrar é o primeiro a sair
print(filaComLista.__str__()) 

# saída print: 0 - 10
# saída print: 1 - 23
# saída print: 2 - 143


# saída print: 0 - 23
# saída print: 1 - 143

