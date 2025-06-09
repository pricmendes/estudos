# Criando um grafo não direcionado usando um dicionário
grafo_usuarios = {
    'Maria Eduarda': {'Carlito', 'Serafina'},
    'Carlito': {'Maria Eduarda', 'Serafina'},
    'Serafina': {'Maria Eduarda', 'Carlito'}
}

# Função para adicionar uma amizade (aresta) ao grafo
def novo_amigo(grafo, usuario1, usuario2):
    # Garante que os usuários estejam presentes no grafo
    if usuario1 not in grafo:
        grafo[usuario1] = set()
    if usuario2 not in grafo:
        grafo[usuario2] = set()

    grafo[usuario1].add(usuario2)
    grafo[usuario2].add(usuario1)

# Adicionando uma nova amizade (por exemplo, Mário é amigo de Maria Eduarda)
novo_amigo(grafo_usuarios, 'Maria Eduarda', 'Mário')

# Exibindo o grafo
for usuario, amigos in grafo_usuarios.items():
    print(f'\n{usuario} é amigo(a) de: {", ".join(amigos)}\n')


# Output: 
# 
# Maria Eduarda é amigo(a) de: Mário, Serafina, Carlito
# 
# 
# Carlito é amigo(a) de: Maria Eduarda, Serafina
# 
# 
# Serafina é amigo(a) de: Maria Eduarda, Carlito
# 
# 
# Mário é amigo(a) de: Maria Eduarda
# 

