import os
import networkx as nx
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def desenharGrafo(corAresta, espessuraAresta, corVertice):
    global contadorFigura
    nx.draw(G, with_labels = True,
        pos = posicionamento,
        edge_color = corAresta,
        width = list(espessuraAresta),
        node_color = corVertice)
    pdf.savefig()
    nomeImagem = "grafo" + str(contadorFigura) + ".jpg"
    contadorFigura += 1
    plt.savefig(nomeImagem)
    plt.show()


def desenhoInicialGrafo():
    global posicionamento
    for n1, n2 in arestas:
        G.add_edge(n1, n2, label = (n1 + "->" + n2), color = "black", weight = 1)
    G.add_nodes_from(vertices, color = "gray")
    corAresta, espessuraAresta = definirAtributos()
    posicionamento = nx.planar_layout(G)
    desenharGrafo(corAresta, espessuraAresta, nx.get_node_attributes(G, "color").values())


def definirAtributos():
    corAresta = nx.get_edge_attributes(G, "color").values()
    espessuraAresta = nx.get_edge_attributes(G, "weight").values()
    return corAresta, espessuraAresta


def atualizarDesenho(v1, v2, corVertice):
    G.get_edge_data(v1, v2)["color"] = "black"
    G.get_edge_data(v1, v2)["weight"] = 4
    corAresta, espessuraAresta = definirAtributos()
    desenharGrafo(corAresta, espessuraAresta, corVertice)


def buscaEmLargura(G, verticeInicial, valorProcurado):
    vetorNiveis = {}
    vetorPredecessoras = {}
    controleVisitadosPorCor = nx.get_node_attributes(G, "color")
    controleVisitadosPorCor[verticeInicial] = "green"
    vetorNiveis[verticeInicial] = 0
    filaControle = [verticeInicial]
    while filaControle:
        verticePai = filaControle.pop(0)
        for verticeEncontrado in G.neighbors(verticePai):
            if controleVisitadosPorCor[verticeEncontrado] == "gray":
                vetorNiveis[verticeEncontrado] = vetorNiveis[verticePai] + 1
                vetorPredecessoras[verticeEncontrado] = verticePai
                filaControle.append(verticeEncontrado)
                if valorProcurado == verticeEncontrado:
                    controleVisitadosPorCor[verticeEncontrado] = "red"
                    atualizarDesenho(verticePai, verticeEncontrado, controleVisitadosPorCor.values())
                    print("Valor ", valorProcurado, " encontrado no nível ", vetorNiveis[valorProcurado]), \
                        ", predecessora: ", vetorPredecessoras[valorProcurado]
                    return
                else:
                    controleVisitadosPorCor[verticeEncontrado] = "green"
                    atualizarDesenho(verticePai, verticeEncontrado, controleVisitadosPorCor.values())


G = nx.DiGraph()
posicionamento = nx.planar_layout(G)
contadorFigura = 1
vertices = ["A", "B", "C", "D", "E", "F", "G"]
arestas = [("A", "B"), ("A", "E"), ("B", "C"), ("E", "D"), ("E", "F"), ("C", "E"), ("F", "D"), ("A", "G"), ("G", "D")]
pdf = PdfPages("GrafoPassoAPasso2.pdf")
desenhoInicialGrafo()

buscaEmLargura(G, "A", "F")
pdf.close()

os.startfile("GrafoPassoAPasso2.pdf")


# link com o PDF - https://1drv.ms/b/s!AsVvE5cfA4mTmuckQKuZyT-9akzAlQ?e=KwSTdq