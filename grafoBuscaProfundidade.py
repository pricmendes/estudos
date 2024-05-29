import os
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_pdf import PdfPages


def desenharGrafo(colors, weights):
    # Função para desenhar o grafo, salvar a imagem em um PDF e salvar cada imagem como .jpg
    global contadorFigura
    plt.figure()  # Criar uma nova figura a cada chamada
    nx.draw(G, with_labels = True, \
            pos = posicionamento, \
            edge_color = colors, \
            width = list(weights), \
            node_color = "red")
    pdf.savefig()
    nomeImagem = "grafo" + str(contadorFigura) + ".jpg"
    contadorFigura += 1
    plt.savefig(nomeImagem)
    plt.close() # Fecha a figura para liberar memória
    # plt.show() # abre as imagens uma a uma


def desenhoInicialGrafo(): # ligação dos grafos
    # Inicializa o grafo com as arestas e atributos padrão (cor e peso)
    global weights, posicionamento
    for n1, n2 in arestas:
        G.add_edge(n1, n2, label = (n1 + "->" + n2), color = "black", weight = 1)
    
    colors, weights = definirAtributos()
    posicionamento = nx.planar_layout(G)
    desenharGrafo(colors, weights)


def definirAtributos(): # cor das arestas
    # Retorna as cores e pesos das arestas
    colors = nx.get_edge_attributes(G, "color").values()
    weights = nx.get_edge_attributes(G, "weight").values()
    return colors, weights


def atualizarDesenho(v1, v2):
    # Atualiza as cores e pesos das arestas durante a busca em profundidade
    global corRedesenho, contadorCor, controleCor
    controleCor = True
    G.get_edge_data(v1, v2)["color"] = corRedesenho[contadorCor]
    G.get_edge_data(v1, v2)["weight"] = 4
    colors, weights = definirAtributos()
    desenharGrafo(colors, weights)


def inicializaVariaveis(): # inicialização e atributos dos valores iniciais
    global valorProfundidadeEntrada, valorProfundidadeSaida, profundidadesEntradaSaida, verticesPai, niveis, \
        controleVertices, demarcadores, verticeComSaidasValidas, corRedesenho, contadorCor, controleCor
    valorProfundidadeEntrada = 0
    valorProfundidadeSaida = 0
    profundidadesEntradaSaida = {}
    verticesPai = {}
    niveis = {}
    controleVertices = {}
    demarcadores = set()
    verticeComSaidasValidas = set()
    corRedesenho = ["red", "green", "blue", "gray"]
    contadorCor = 0
    controleCor = True


def buscaEmProfundidade(vertices, arestas, verticeGrafo):
    # Função principal de busca em profundidade
    inicializaVariaveis()
    grafo = {}
    for v in vertices:
        grafo[v] = []
        for a in arestas:
            if v == a[0]:
                grafo[v].append(a[1])
    for vertice in grafo:
        controleVertices[vertice] = vertice

    verticesPai[verticeGrafo] = None
    quantidadeFilhosRaiz = procuraProximoVertice(grafo, verticeGrafo, 1)
    if quantidadeFilhosRaiz <= 1:
        verticeComSaidasValidas.remove(verticeGrafo)


def procuraProximoVertice(grafo, verticeGrafo, nivel):
    # Procura os próximos vértices na busca em profundidade
    global valorProfundidadeEntrada, valorProfundidadeSaida, contadorCor, controleCor
    valorProfundidadeEntrada += 1
    profundidadesEntradaSaida[verticeGrafo] = [valorProfundidadeEntrada, None]
    niveis[verticeGrafo] = nivel

    contadorFilhos = 0

    for proximoVertice in grafo.get(verticeGrafo):
        if not profundidadesEntradaSaida.get(proximoVertice):
            verticesPai[proximoVertice] = verticeGrafo
            contadorFilhos += 1
            atualizarDesenho(verticeGrafo, proximoVertice)
            procuraProximoVertice(grafo, proximoVertice, nivel + 1)
            if niveis[controleVertices[proximoVertice]] < niveis[controleVertices[verticeGrafo]]:
                controleVertices[verticeGrafo] = controleVertices[proximoVertice]

            if proximoVertice in demarcadores:
                verticeComSaidasValidas.add(verticeGrafo)
        else: # Atualiza a variável controleVertice se já foi visitado
            if not profundidadesEntradaSaida[proximoVertice][1]:
                if verticesPai[verticeGrafo] != proximoVertice:
                    if niveis[proximoVertice] < niveis[controleVertices[verticeGrafo]]:
                        controleVertices[verticeGrafo] = proximoVertice

    valorProfundidadeSaida += 1
    profundidadesEntradaSaida[verticeGrafo][1] = valorProfundidadeSaida
    if controleVertices[verticeGrafo] in (verticeGrafo, verticesPai[verticeGrafo]):
        demarcadores.add(verticeGrafo)
        if controleCor:
            contadorCor += 1
            controleCor = False

    return contadorFilhos
    
# Inicializa o grafo e outras variáveis necessárias
G = nx.DiGraph() 
contadorFigura = 1
pdf = PdfPages("GrafoPassoAPasso.pdf")
vertices = ["A", "B", "C", "D", "E", "F", "G"]
arestas = [("A", "B"), ("A", "E"), ("B", "C"), ("E", "D"), ("E", "F"), ("C", "E"), ("F", "D"), ("A", "G"), ("G", "D")]

# Desenha o grafo inicial
desenhoInicialGrafo()

# Executa a busca em profundidade a partir do vértice "A"
buscaEmProfundidade(vertices, arestas, "A")

# Fecha o PDF após desenhar todos os passos
pdf.close()

# Abre o PDF automaticamente após salvá-lo
os.startfile("GrafoPassoAPasso.pdf")  # Para Windows

# link com o PDF - https://1drv.ms/b/s!AsVvE5cfA4mTmucPID5fLdgLMN9srQ?e=7zCKyR
