grafoExplicito = {"A" : ["B"],
                  "B" : ["C", "D"],
                  "C" : ["B", "E"],
                  "D" : ["A"],
                  "E" : ["B"]}

# Função para imprimir o grafo sem colchetes
def print_grafo(grafo):
    print("Grafos Explícitos: ")
    for chave, valor in grafo.items():
        print(f"{chave} : {", ".join(valor)}")  # Converte os elementos da lista para strings e junta com vírgulas

print("\n-----------------------------\n")
print_grafo(grafoExplicito)
print("\n-----------------------------\n")
print("Quantidade de Grafos Explícitos: ", len(grafoExplicito))  # Usa len() diretamente para obter o comprimento
print("\n-----------------------------\n")


# Output:
# -----------------------------

# Grafos Explícitos: 
# A : B
# B : C, D
# C : B, E
# D : A
# E : B
# 
# -----------------------------
# 
# Quantidade de Grafos Explícitos:  5
# 
# -----------------------------