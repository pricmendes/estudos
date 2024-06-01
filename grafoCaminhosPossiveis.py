import networkx as nx
import matplotlib.pyplot as plt


def caminhosPossiveis(grafo, proximo, alvo):
    global caminhos, possibilidades
    for aresta in list(filter(lambda filtro: (filtro[0] == proximo), grafo.edges)):
        if aresta[0] == proximo:
            caminhos.append(aresta)
            if aresta[1] == alvo:
                possibilidades.append(caminhos.copy())
                caminhos.pop()
            else:
                caminhosPossiveis(grafo, aresta[1], alvo)
    if len(caminhos) > 0:
        caminhos.pop()


def montarRastreioVertices(trajeto, vertice):
    if trajeto not in vertice:
        vertice.append(trajeto)


def dijkstra(grafo, origem, alvo):
    caminhosPossiveis(grafo, origem, alvo)
    menor = -1
    for percurso in possibilidades:
        soma = 0
        vertice = []
        for trajeto in percurso:
            soma =+ nx.get_edge_attributes(G, "length")[trajeto]
            montarRastreioVertices(trajeto[0], vertice)
            montarRastreioVertices(trajeto[1], vertice)
        if menor == -1 or menor > soma:
            menor = soma
            encontrado["rastro"] = vertice
            encontrado["percurso"] = percurso
            encontrado["distancia"] = menor

def criarGrafo():
    global arestas, labels, vertices
    arestas = [("A", "B"), ("A", "E"), ("B", "C"), ("E", "D"), ("E", "F"), ("C", "E"), ("F", "D"), ("A", "G"), ("G", "D")]
    labels = {("A", "B"): 10, ("A", "E"): 9, ("B", "C"): 2, ("E", "D"): 5, ("E", "F"): 6, ("C", "E"): 2, ("F", "D"): 2, ("A", "G"): 9, ("G", "D"): 1}
    vertices = ["A", "B", "C", "D", "E", "F", "G"]
    for n1, n2 in arestas:
        G.add_edge(n1, n2, length = labels[(n1, n2)], color = "black", weight = labels[(n1, n2)])
    G.add_nodes_from(vertices, color = "gray")
    posicionamento = nx.planar_layout(G)
    nx.draw_networkx_edge_labels(G, posicionamento, edge_labels=nx.get_edge_attributes(G, "length"), font_color="blue")
    nx.draw(G, with_labels = True, pos = posicionamento)
    plt.show()


labels = {}
arestas = {}
vertices = []
encontrado = {}
caminhos = []
possibilidades = []
G = nx.DiGraph()
criarGrafo()

verticePartida = "A"
verticeDestino = "D"

dijkstra(G, verticePartida, verticeDestino)
print("\nRastreio: ", encontrado["rastro"])
print("\nPercurso: ", encontrado["percurso"])
print("\nDistância Percorrida: ", encontrado["distancia"])
print("\nBiblioteca Networkx")
print("\nRastreio na biblioteca: ", nx.shortest_path(G, verticePartida, verticeDestino, "length"))
print("\nDistância Percorrida: ", nx.shortest_path_length(G, verticePartida, verticeDestino, "length"))


# Função criarGrafo() define um grafo direcionado com arestas, rótulos e vértices.
# Função dijkstra() executa o algoritmo de Dijkstra para encontrar o menor caminho em um grafo.
# Usa uma função recursiva (caminhosPossiveis) para encontrar todos os caminhos possíveis entre dois vértices.
# Compara a distância de cada caminho e armazena o caminho mais curto encontrado.


# Output:
# Link da imagem gerada: https://i.imgur.com/oaMj0Ll.png
# Rastreio:  ['A', 'G', 'D']
#
# Percurso:  [('A', 'G'), ('G', 'D')]
#
# Distância Percorrida:  1
#
# Biblioteca Networkx
#
# Rastreio na biblioteca:  ['A', 'G', 'D']
#
# Distância Percorrida:  10
