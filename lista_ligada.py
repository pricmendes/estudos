from elemento_lista import ElementoUnicoDaLista


class ListaLigada:
    def __init__(self): # construtor da classe
        self._inicio = None # a partir deste elemento saberemos qual será o próximo elemento
        self._quantidade = 0 # mantém a quantidade da lista, permitindo que a qualquer momento possamos saber quantos elementos estão na lista

    @property # define que um atributo terá um método para recuperar a informação.
    def inicio(self):
        return self._inicio # retorna o valor do atributo "inicio"
        
    @property
    def quantidade(self):
        return self._quantidade # retorna o valor do atributo "quantidade"
    
    def inserirNoInicioLista(self, conteudo): # inclui 1 elemento na lista
        elemento = ElementoUnicoDaLista(conteudo) # armazena o elemento
        elemento.proximoElemento = self._inicio # posiciona o elemento na lista
        self._inicio = elemento # Informa quem é o primeiro elemento agora
        self._quantidade += 1 # aumenta a quantidade do elemento
        
    def inserir(self, posicao, conteudo): # insere um elemento em qualquer posição da lista
        if posicao == 0:
            self.inserirNoInicioLista(conteudo)
            return
        elemento = ElementoUnicoDaLista(conteudo)
        esquerda = self._elemento(posicao - 1) # crescimento da esquerda para a direita
        elemento.proximoElemento = esquerda.proximoElemento
        esquerda.proximoElemento = elemento
        self._quantidade += 1 # adiciona um número a quantidade de elementos
    def _elemento(self, posicao):
        self._validarPosicao(posicao) # verifica se a posição é válida
        atual = self.inicio
        for i in range(0, posicao):
            atual = atual.proximoElemento
        return atual
    def _validarPosicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError("Posição inválida {posicao}")
    
    def removerDoInicio(self): # remover elementos no início da fila
        removido = self.inicio
        self._inicio = removido.proximoElemento # informa que o elemento do início mudou
        removido.proximoElemento = None
        self._quantidade -= 1 # diminui elementos da lista
        return removido.elementoDaLista # retorna o elemento que foi removido
    
    def remover(self, posicao):
        esquerda = self._elemento(posicao - 1)
        removido = esquerda.proximoElemento
        esquerda.proximoElemento = removido.proximoElemento
        removido.proximoElemento = None
        self._quantidade -= 1
        return removido.elementoDaLista # retorna o elemento que foi removido
    
    def buscaElemento(self, posicao):
        self._validarPosicao(posicao)
        elemento = self._elemento(posicao)
        return elemento.elementoDaLista
    
    def imprimir(self): # imprimir todos os elementos da lista
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.elementoDaLista)
            atual = atual.proximoElemento
            
            

        