from lista_duplamente_ligada import ListaDuplamenteLigada


class Loja:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def __repr__(self):
        return "{}\n {}".format(self._nome, self._endereco)


def statusLista(lista):
    print(lista.quantidade)
    lista.imprimir()


def main():
    loja1 = Loja("Mercadinho do Zé", "Rua das frutas frescas, 1234")
    loja2 = Loja("Direto do Colono", "Rua do Colono, 10000")
    loja3 = Loja("Quitanda do Bairro", "Rua das Cebolas, 9999")
    loja4 = Loja("Boa Fruta", "Rua Eureka, 13254")
    loja5 = Loja("Horti Agora", "Rua da Praia, 5464")
    loja6 = Loja("Fruti-Fruti", "Av. dos Verdes, 5")
    lista = ListaDuplamenteLigada()
    lista.inserir(loja1)
    lista.inserir(loja2)
    statusLista(lista)
    lista.inserir(1, loja3)
    statusLista(lista)
    lista.inserir(1, loja4)
    lista.inserir(1, loja5)
    lista.inserir(3, loja6)
    statusLista(lista)
    print("\n")
    print("Consultando o índice 3{}".format(lista.buscaElemento(2)))
    print("Consultando o índice 4{}".format(lista.buscaElemento(4)))
    print("\n------ REMOVER ------")
    lista.remover(0)
    statusLista(lista)
    lista.remover(lista.quantidade - 1)
    statusLista(lista)
    lista.remover(1)
    statusLista(lista)
    lista.remover(0)
    lista.remover(0)
    lista.remover(0)
    statusLista(lista)


main()
