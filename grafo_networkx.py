import networkx as bibliotecaNetworkx # importa a biblioteca

grafo = bibliotecaNetworkx.Graph() # instala o objeto como um grafo

grafo.add_node("A") # Adiciona vértices
grafo.add_node("B")
grafo.add_node("C")
grafo.add_node("D")


grafo.add_edge("A", "B") # Adiciona as arestas
grafo.add_edge("A", "C")
grafo.add_edge("B", "D")
grafo.add_edge("C", "D")
grafo.add_edge("C", "B")

numeroVertices = grafo.number_of_nodes()
numeroArestas = grafo.number_of_edges()
print("\nVisualizando as ligações do vértice A:", grafo.adj["A"], "\n")
print("Quantidade de arestas por vértice", grafo.degree, "\n")
print("Quantidade de vértices: ", numeroVertices, "\n")
print("Quantidade de arestas: ", numeroArestas, "\n")
print("Vértices do grafo: ", grafo.nodes(), "\n")
print("Arestas dos vértices:", grafo.edges, "\n")

# Output:
# 
# Visualizando as ligações do vértice A: {'B': {}, 'C': {}} 
# 
# Quantidade de arestas por vértice [('A', 2), ('B', 3), ('C', 3), ('D', 2)] 
# 
# Quantidade de vértices:  4 
# 
# Quantidade de arestas:  5 
# 
# Vértices do grafo:  ['A', 'B', 'C', 'D'] 
# 
# Arestas dos vértices: [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'C'), ('C', 'D')] 
