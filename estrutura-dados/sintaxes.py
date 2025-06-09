# comentário 1 linha
"""
teste comentário várias linhas
"""
# =================================================================================


nome = "Priscila" + \
" Cardoso"
print()
print(nome)
print("exemplo 1: ---------------")
print()
print("\n============================================================\n")
print()

# =================================================================================


idade = 25

if idade < 18:
    print("menor de idade")
else:
    print("maior de idade")
print("exemplo 2: ---------------")
print()
print("\n============================================================\n")
print()

# =================================================================================


nome_completo = "Priscila" 

idade = 40

nomeCompleto = "Cardoso"

print(nome_completo, nomeCompleto,"tem a idade de", idade, "anos")
print("exemplo 3: ---------------")
print()
print("\n============================================================\n")
print()

# =================================================================================


nomeCompleto.find("a")
print(nomeCompleto.find("a"))
print()
print("\n============================================================\n")
print()

# =================================================================================
# listas

minha_lista = [1, 2, 3, 4, 5, "Priscila", True, False]

minha_lista[0] = "python"

print("Minha lista de exemplo", minha_lista)
print()
print("Minha Lista Índice [0]:", minha_lista[0])
print()
print("Minha Lista Índice [5]:", minha_lista[5])
print()
print("Minha Lista Índice [1:7]:", minha_lista[1:7])
print()
print("Minha Lista Índice [:5]:", minha_lista[:5])
print()

# método de listas

# "APPEND" - adiciona um elemento ao final da lista

minha_lista.append(6)
print("Após append (6)", minha_lista)
print()

# INDEX - retornar o índice do primeiro elemento = ao valor especificado

indice = minha_lista.index("Priscila")
print("Após índice (Priscila)", indice)
print()

# INSERT = insere um elemento em um índice específico

minha_lista.insert(2, 10) # trocou o 2 pelo 10
print("Após o insert(de 2 para 10)", minha_lista)
print()

# pop - remove e retorna um elemento de um índice específico

elemento_devido = minha_lista.pop(3) # remove o elemento anterior no caso do índice 2
print("Elemento removido:", elemento_devido)
print("Após o pop(3)", minha_lista)
print()

# remove - remove o elemente específicado

minha_lista.remove(True)
print("Após remove(True):", minha_lista)
print()

# SORT - organiza a lista em ordem crescente- só funciona se os itens da lista forem do mesmo padráo de valor - exemplo tipo int, tipo string, tipo bolleano

minha_lista_int = [1, 10, 5, 6, 2, 9, 8, 6, 2, 3, 9, 12]

minha_lista_int.sort()
print("Após sort()", minha_lista_int)
print()

minha_lista_string = ["b", "c", "d", "f", "r", "g", "h", "j", "e", "a", "m", "p", "i", "l", "u", "y", "z", "x"]
minha_lista_string.sort()
print("Após sort()", minha_lista_string)
print()
print("\n============================================================\n")
print()

# =================================================================================

# TUPLAS

minha_tupla = (1, 2, 3, 4, 5)

print("Minha Tupla:", minha_tupla)
print()
print("Minha Tupla (0):", minha_tupla[0])
print()
print("Minha Tupla (2):", minha_tupla[2])
print()
print("Minha Tupla (-1):", minha_tupla[-1])
print()

# COUNT
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)
print()

# INDEX
indice = minha_tupla.index(3)
print("Índice da primeira ocorrência do elemento 3:", indice)
print()
print("\n============================================================\n")
print()

# =================================================================================

# DICIONÁRIOS
# CRIANDO UM DICIONÁRIO
print("Dicionários")
pessoa = {"nome": "Priscila", "idade": 40, "cidade": "Barueri-SP"}

# EXIBINDO O DICIONÁRIO
print("Meu dicionário exemplo:", pessoa)
print()

# ACESSANDO VALORES POR CHAVE
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Cardoso"
print("Sobrenome:", pessoa["sobrenome"])
print("\n============================================================\n")
print()

# =================================================================================

# Manipulando um dicionário
print("Manipulando dicionários")
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])
print("Meu dicionário exemplo:", pessoa)
print()


# removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário exemplo:", pessoa)
print()

# KEYS(), VALUES(), ITEMS()

chaves = pessoa.keys()
print("Chaves do dicionário:", chaves)
print()

chaves = list(pessoa.keys())
print("Primeira chave do dicionário:", chaves[0])
print()

valores = pessoa.values()
print("Valores do dicionário:", valores)
print()

valores = list(pessoa.values())
print("Primeiro valor do dicionário:", valores[0])
print()

itens = pessoa.items()
print("Itens do dicionário:", itens)
print()

itens = list(pessoa.items())
print("Primeiro item do dicionário:", itens[0][1])
print()

itens = list(pessoa.items())
print("Primeiro e segundo itens do dicionário: %s = %s " % (itens[0][0], itens[0][1]))
print()


print("\n============================================================\n")
print()

# =================================================================================

# CONDICIONAIS
# if, elif, else

idade = 19

print("Exemplo de comando if.")
print()
if idade >= 18:
    print("Você é maior de idade.")
print()

if idade == 19:
    print("Você tem 19 anos.")
print()

if idade < 18:
    print("Você é menor de idade.")
print()

if idade != 10:
    print("Você não tem 10 anos.")
print()

print("\n============================================================\n")
print()

idade = 18

print("Exemplo de comando else.")
print()
if idade >= 18:
    print("Você é maior de idade.")

else:
    print("Você é menor de idade.")
print()

print("\n============================================================\n")
print()

idade = 10

print("Exemplo de comando elif.")
print()
if idade >= 18:
    print("Você é maior de idade.")

elif idade >= 11:
    print("Você é adolescente.")
elif idade <= 10:
    print("Você é criança.")
else:
    print("Você é menor de idade.")
print()

print("\n============================================================\n")
print()


idade = 17

print("Exemplo de comando if, elif e else numa única linha.")
print()

mensagem = "Pode tirar a carteira de habilitação." if idade >= 18 else f"Você não pode tirar a carteira de habilitação ainda. Sua idade é: {idade}"
print(mensagem)
print()

print("\n============================================================\n")
print()

# =================================================================================

# Entrada de dados (INPUT)

# idade = int(input("Quantos você tem? "))
# print()
# mensagem = f"Você pode tirar a carteira de habilitação. Você tem {idade} anos." if idade >= 18 else f"Você não pode tirar a carteira de habilitação ainda. Sua idade é: {idade}."
# print(mensagem)
# print()
#               
# 
# print("\n============================================================\n")
# print()

# =================================================================================

# LOOP FOR
# FOR repete a mesma ação para uma sequência de elementos - listas, tuplas, dicionários

print("FOR utilizando lista.")
print()
lista = [1, 2, 3, 4, 5, "Priscila", "Cardoso"]
for elemento in lista:
    print(elemento) # irá imprimir um em cada linha 
print()

print("FOR utilizando tupla.")
print()
tupla = (1, 2, 3, 4, 5, "Priscila", "Cardoso")
for elemento in tupla:
    print(elemento) # irá imprimir um em cada linha 
print()

print("\nFOR utilizando dicionário/chaves.")
print()
pessoa = {"nome": "Priscila", "idade": 40, "cidade": "Barueri-SP"}
for chave in pessoa.keys():
    print(chave)
print()

print("\nFOR utilizando dicionário/valores.")
for elemento in pessoa.values():
    print(elemento)
print()

print("\nFOR utilizando dicionário/itens.")
for itens in pessoa.items():
    print(itens)
print()

print("\nFOR utilizando dicionário/itens. Modelo com f.")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
print()

# range() - retorna um intervalo numérico em forma de lista
print("\nRange Exemplos.")
print()

print(list(range(0, 10)))
print()
print("Range tilizando variáveis:")
print()
for numero in range(5):
    print("Números:", numero)
print()

print("\n Utilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    print()
    print("Índice:", indice)
    print("Elemento", lista[indice])
    print()
    if indice == 3:
        lista[indice] = 5
    print(lista)
print()

# enumerate

print("Enumerate")
print()
lista_enumerate = ["a", "b", "c", "d", "e"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Índice 1 ")


# LOOP WHILE
print("\nLoop While")
print("\nExemplos de while:")
print()
contador = 0
while contador < len(lista):
    print("Contagem:", contador)
    contador = contador + 1
    print()

print("\n2")
contador = 0
while contador < 5:
    print("Contagem:", contador)
    contador += 1 # para finalizar o while

print("\nPrograma Finalizado.\n")


print("\n============================================================\n")


# =================================================================================

# FUNÇÕES

print("\nTipos Funções:\n")

def saudacao(nome):
    print(f"Olá, {nome}!")

print("\nChamando a função saudação:")
saudacao("Alice")
saudacao("Bob")

# Função com retorno
print("\nFunção com retorno exemplo:\n")
def quadrado(numero):
    resultado = numero ** 2 # dois asteriscos significa o número ao quadrado
    return resultado

resultado_quadrado = quadrado(6)
print(f"\nResultado da função quadrado: ", resultado_quadrado, "\n")

# Função com múltiplos parâmetros
print("\nFunção com múltiplos parâmetros exemplos:\n")
print("****** Exemplo 1: ******")
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
print("\nFunção soma múltiplos parâmetros:\n")
resultado_soma = soma(20, 50)
print("\nA soma do número 20 e número 50 é:", resultado_soma, "\n")

print("****** Exemplo 2: ******")
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
print("\nFunção soma múltiplos parâmetros:\n")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("\nA soma do número %s e número %s é %s:" %(numero1, numero2, resultado_soma))

print("\n============================================================\n")


