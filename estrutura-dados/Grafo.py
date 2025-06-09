from collections import defaultdict

class grafo(object): # início do grafo direcionado
    def __init__(self, aresta, direcionado = False):
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adicionar_aresta(aresta)

    def get_vertice(self): # lista dos vértices
        return list(self.adj.keys())

    def get_aresta(self): # lista das arestas
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adicionar_aresta(self, aresta): # adiciona aresta
        for u, v in aresta:
            self.adiciona_ligacao(u, v)

    def adiciona_ligacao(self, u, v): # ligação entre vértices
        self.adj[u].add(v)
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v): # verifica arestas
        return u in self.adj and v in self.adj[u]

    def __len__(self): # tamanho do grafo
        return len(self.adj)

    def __str__(self): # impressão dos grafos
        return "{} ({})".format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v): # lista adjacentes do vértice
        return self.adj[v]

