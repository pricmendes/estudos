grafoImplicito = [ [1],
                   [2, 3],
                   [1, 4],
                   [0],
                   [1]]

# Função para imprimir o grafo sem colchetes
def print_grafo(grafo):
    print("Grafos Implícitos: ")
    for lista in grafo:
        print(", ".join(map(str, lista)))  # Converte cada elemento para string e junta com vírgulas

print("\n-----------------------------\n")
print_grafo(grafoImplicito)
print("\n-----------------------------\n")
print("Quantidade de Grafos Implícitos: ", len(grafoImplicito))  # Usa len() diretamente para obter o comprimento
print("\n-----------------------------\n")

# Output:
# -----------------------------
# 
# Grafos Implícitos: 
# 1
# 2, 3
# 1, 4
# 0
# 1
# 
# -----------------------------
# 
# Quantidade de Grafos Implícitos:  5
#
#-----------------------------