from lista_ligada import ListaLigada, ElementoUnicoDaLista


class Loja:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def __repr__(self):
        return "{}\n {}".format(self._nome, self._endereco)
    

def main():
    loja1 = Loja("Mercadinho do Zé", "Rua das frutas frescas, 1234")
    loja2 = Loja("Direto do Colono", "Rua do Colono, 10000")
    loja3 = Loja("Quitanda do Bairro", "Rua das Cebolas, 9999")
    loja4 = Loja("Boa Fruta", "Rua Eureka, 13254")
    loja5 = Loja("Horti Agora", "Rua da Praia, 5464")
    loja6 = Loja("Fruti-Fruti", "Av. dos Verdes, 5")
    lista = ListaLigada()
    lista.inserirNoInicioLista(loja1)
    lista.inserirNoInicioLista(loja2)
    lista.inserirNoInicioLista(loja3)
    lista.inserir(1, loja4)
    lista.inserir(0, loja5)
    lista.inserir(lista.quantidade, loja6)
    print(lista.quantidade)
    lista.imprimir()
    removido = lista.removerDoInicio()
    print(lista.quantidade)
    print(f"Removido: {removido}")
    print("\n")
    print(lista.quantidade)
    lista.imprimir()
    print("----------")
    print("elemento removido {}".format(lista.remover(2)))
    print("\n")
    print(lista.quantidade)
    lista.imprimir()
    print("\n\nEncontrando o elemento 2: {}".format(lista.buscaElemento(1)))

main()



# output: 6
# output: Horti Agora
# output:  Rua da Praia, 5464
# output: Quitanda do Bairro
# output:  Rua das Cebolas, 9999
# output: Boa Fruta
# output:  Rua Eureka, 13254
# output: Direto do Colono
# output:  Rua do Colono, 10000
# output: Mercadinho do Zé
# output:  Rua das frutas frescas, 1234
# output: Fruti-Fruti
# output:  Av. dos Verdes, 5
# output: 5
# output: Removido: Horti Agora
# output:  Rua da Praia, 5464
# output: 
# output: 
# output: 5
# output: Quitanda do Bairro
# output:  Rua das Cebolas, 9999
# output: Boa Fruta
# output:  Rua Eureka, 13254
# output: Direto do Colono
# output:  Rua do Colono, 10000
# output: Mercadinho do Zé
# output:  Rua das frutas frescas, 1234
# output: Fruti-Fruti
# output:  Av. dos Verdes, 5
# output: ----------
# output: elemento removido Direto do Colono
# output:  Rua do Colono, 10000
# output: 
# output: 
# output: 4
# output: Quitanda do Bairro
# output:  Rua das Cebolas, 9999
# output: Boa Fruta
# output:  Rua Eureka, 13254
# output: Mercadinho do Zé
# output:  Rua das frutas frescas, 1234
# output: Fruti-Fruti
# output:  Av. dos Verdes, 5
# output: 
# output: 
# output: Encontrando o elemento 2: Boa Fruta
# output:  Rua Eureka, 13254