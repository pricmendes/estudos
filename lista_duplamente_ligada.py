from elemento_lista_2 import Elemento # impportar a classe Elemento da lista elemento_lista_2


class ListaDuplamenteLigada:
    def __init__(self):
        self._primeiro: Elemento = None # controla o elemento da primeira posição
        self._ultimo: Elemento = None # controla o elemento da última posição
        self._quantidade = 0 # quantidade de elementos na lista
# recuperar os dados armazenados nos atributos
    @property
    def primeiro(self):
        return self._primeiro

    @property
    def ultimo(self):
        return self._ultimo

    @property
    def quantidade(self):
        return self._quantidade

    def _adicionaQuantidade(self):
        self._quantidade += 1
        
    def _diminuiQuantidade(self):
        self._quantidade -= 1

    def _inserirListaVazia(self, elemento): # armazena os atributos na lista
        self._primeiro = elemento
        self._ultimo = elemento
        self._adicionaQuantidade()

    def _inserirNoInicio(self, conteudo):
        elementoAtual = Elemento(conteudo)
        if self._quantidade == 0: # se a lista estiver vazia será inserido os dados
            return self._inserirListaVazia(elementoAtual)
        elementoAtual.proximo = self._primeiro
        self._primeiro.anterior = elementoAtual # define quem é o anterior e insere após
        self._primeiro = elementoAtual # substitui o primeiro elemento para ser o anterior
        self._adicionaQuantidade() # inserindo o elemento atual como o primeiro

    def _inserirNoFim(self, conteudo): # insere no final da lista caso a lista esteja vazia
        elementoAtual = Elemento(conteudo)
        if self._quantidade == 0
            return self._inserirListaVazia(elementoAtual) # inserindo valores do elemento anterior
        elementoAtual.anterior = self._ultimo
        self._ultimo.proximo = elementoAtual # atualiza o valor do próximo elemento
        self._ultimo = elementoAtual # substitui o valor do último elemento
        self._adicionaQuantidade()

    def inserir(self, posicao, conteudo): # inseri e verifica se a posição é primeira ou última
        if posicao == 0
            return self._inserirNoInicio(conteudo)
        if posicao >= (self.quantidade - 1)
            return self._inserirNoFim(conteudo)

        elementoAtual = Elemento(conteudo) # elemento ainda não tem posição
        elementoDireita = self._elemento(posicao) # elemento a direita para crescer positivo
        elementoEsquerda = elementoDireita.anterior # atribui o elemento à esquerda

        elementoAtual.proximo = elementoDireita # liga os elementos direita e esquerda
        elementoAtual.anterior = elementoEsquerda

        elementoEsquerda.proximo = elementoAtual
        elementoDireita.anterior = elementoAtual
        self._adicionaQuantidade()

    def _validarPosicao(self, posicao): # verifica se o valor não extrapola o limite da lista
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError(f"Posição inválida {posicao}")

    def _elemento(self, posicao): # busca o elemento pela posição
        self._validarPosicao(posicao)
        metade = self.quantidade // 2 # coleta a informação do índice que está no meio da lista e retorna somente valor inteiro mesmo que a divisão não seja exata
        if posicao < metade: # verifica se a posição está na metade superior ou na metade inferior para encontrar ele mais rapidamente
            print("*** busca na metade inferior - metade: {}, posição: {}***".format(metade, posicao))
            atual = self._buscaElementoMenorMetade(posicao)
        else:
            print("*** busca na metade superior - metade: {}, posição: {}***".format(metade, posicao))
            atual = self._buscaElementoMaiorMetade(posicao)
        return atual

    def _buscaElementoMaiorMetade(self, posicao): # realiza a busca se estiver na metade maior
        atual = self.ultimo
        for i in range(posicao + 1, self.quantidade)[:: - 1]:
            atual = atual.anterior
        return atual

    def _buscaElementoMenorMetade(self, posicao): # realiza a busca se estiver na metade menor
        atual = self._primeiro
        for i in range(0, posicao):
            atual = atual.proximo
        return atual

    def _removerUltimo(self): # método para remover o último elemento da lista
        elementoRemovido = self.ultimo
        novoUltimo = elementoRemovido.anterior # o elemento que será o último
        novoUltimo.proximo = novoUltimo
        self._ultimo = novoUltimo
        elementoRemovido._anterior = elementoRemovido._proximo = None # informações de quem será anterior e próximoas são limpas do elemento removido
        self._diminuiQuantidade()
        return elementoRemovido.conteudoElemento

    def _removerPrimeiro(self): # método para remover o primeiro da lista e verificar se o primeiro é o último para tratar lista vazia
        if self.quantidade == 1:
            return self._esvaziarLista()
        elementoRemovido = self.primeiro # recupera o elemento a ser removido que é o primeiro da lista
        novoPrimeiro = elementoRemovido.proximo # novo primeiro
        novoPrimeiro.anterior = None
        self._primeiro = novoPrimeiro
        elementoRemovido.anterior = elementoRemovido.proximo = None # o elemento que foi removido tem os atributos do anterior e próximos limpos, diminui a quantidade de elementos
        self._diminuiQuantidade()
        return elementoRemovido.conteudoElemento

    def _esvaziarLista(self): # método para tratar lista vazia
        if self._quantidade == 1:
            elementoRemovido = self.primeiro
            self._primeiro = None
            self._ultimo = None
            elementoRemovido.anterior = elementoRemovido.proximo = None
            self._diminuiQuantidade()
            return elementoRemovido.conteudoElemento

    def remover(self, posicao): # método remoção por posição
        if posicao == 0
            return self._removerPrimeiro()
        if posicao >= (self.quantidade - 1):
            return self._removerUltimo()
        elementoRemovido = self._elemento(posicao)# identifica elemento a ser excluído
        elementoEsquerda = elementoRemovido.anterior
        elementoDireita = elementoRemovido.proximo
        elementoEsquerda.proximo = elementoDireita # reconfigura os elementos da esquerda para direita
        elementoDireita.anterior = elementoEsquerda
        elementoRemovido.proximo = None # os atributos removidos são limpos atualiza qtd
        elementoRemovido.anterior = None
        self._diminuiQuantidade()
        return elementoRemovido.conteudoElemento

    def buscaElemento(self, posicao): # método busca posição e retorna o valor
        elemento = self._elemento(posicao)
        return elemento.conteudoElemento

    def imprimir(self): # método imprimir os dados
        atual = self.primeiro
        for i in range(0, self.quantidade):
            print(atual.conteudoElemento)
            atual = atual.proximo




