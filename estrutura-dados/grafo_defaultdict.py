from Grafo import grafo

aresta = [("A", "B"), ("B", "C"), ("C", "B"), ("D", "A"), ("E", "B")] # criação das arestas

criargrafo = grafo(aresta, direcionado = True) # inicializa os grafos

print("\n-----------------------------\n")
print("Grafos: ", criargrafo.adj) # imprime os grafos

print("\n-----------------------------\n")
print("Vértices:", criargrafo.get_vertice()) # imprime os vértices

print("\n-----------------------------\n")
print("Arestas:", criargrafo.get_aresta()) # imprime as arestas

print("\n-----------------------------\n")
print("Existe Aresta A / B? ", criargrafo.existe_aresta("A", "B")) # verdadeiro ou falso

print("\n-----------------------------\n")
print("Existe Aresta E / C? ", criargrafo.existe_aresta("E", "C")) # verdadeiro ou falso

print("\n-----------------------------\n")

# Output:
# -----------------------------
# 
# Grafos:  defaultdict(<class 'set'>, {'A': {'B'}, 'B': {'C'}, 'C': {'B'}, 'D': {'A'}, 'E': {'B'}})
# 
# -----------------------------
# 
# Vértices: ['A', 'B', 'C', 'D', 'E']
# 
# -----------------------------
# 
# Arestas: [('A', 'B'), ('B', 'C'), ('C', 'B'), ('D', 'A'), ('E', 'B')]
# 
# -----------------------------
# 
# Existe Aresta A / B?  True
# 
# -----------------------------
# 
# Existe Aresta E / C?  False
# 
# -----------------------------