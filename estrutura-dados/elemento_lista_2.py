class Elemento:
    def __init__(self, conteudo):
        self.conteudoElemento = conteudo
        self.proximo: Elemento = None
        self.anterior: Elemento = None
