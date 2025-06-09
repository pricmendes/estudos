print("Definição de Vetores\n")

def main():
		vetorVazio = []
		vetorVazio2 = list

		#imprime o tamanho do vetor
		print("Tamanho do vetor vazio é: ", len(vetorVazio))
		for i in range(10):
			#acrescentando um valor no final do vetor
			vetorVazio.append(i)

		print("Novo tamanho do vetor vazio é: ", len(vetorVazio))
		print("Valores agora no vetor vazio são: ", vetorVazio)

		vetorInteiros =  [1, 2, 3, 4, 5, 6, 7]


		#imprime [1, 2, 3, 4, 5, 6, 7]
		print("Valores dos vetores inteiros são: ", vetorInteiros) #retirei[i] antes vetorInteiros[i]) depois vetorInteiros)

		for i in range(0, len(vetorInteiros)):
			#imrpime a posição e o valor da posição
			print("O valor na posição ", i, " é ", vetorInteiros[i])

		vetorCaracteres = ["Maria", "Gui", "Jô", "Edu", "João", "Carlos", "Joaquina"]

		for i in range(len(vetorCaracteres[i])):
			print("O valor na posição ", i, " é ", vetorCaracteres) #retirei[i] antes vetorCaracteres[i]) depois vetorCaracteres)

		vetoresReais = [1.2, 3.5, 12.3, 4.2]
		print("Valores nos vetores reais são: ", vetoresReais)

main()


# saída print: Definição de Vetores
# saída print: 
# saída print: Tamanho do vetor vazio é:  0
# saída print: Novo tamanho do vetor vazio é:  10
# saída print: Valores agora no vetor vazio são:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# saída print: Valores dos vetores inteiros são:  [1, 2, 3, 4, 5, 6, 7]
# saída print: O valor na posição  0  é  1
# saída print: O valor na posição  1  é  2
# saída print: O valor na posição  2  é  3
# saída print: O valor na posição  3  é  4
# saída print: O valor na posição  4  é  5
# saída print: O valor na posição  5  é  6
# saída print: O valor na posição  6  é  7
# saída print: O valor na posição  0  é  ['Maria', 'Gui', 'Jô', 'Edu', 'João', 'Carlos', 'Joaquina']
# saída print: O valor na posição  1  é  ['Maria', 'Gui', 'Jô', 'Edu', 'João', 'Carlos', 'Joaquina']
# saída print: O valor na posição  2  é  ['Maria', 'Gui', 'Jô', 'Edu', 'João', 'Carlos', 'Joaquina']
# saída print: O valor na posição  3  é  ['Maria', 'Gui', 'Jô', 'Edu', 'João', 'Carlos', 'Joaquina']
# saída print: O valor na posição  4  é  ['Maria', 'Gui', 'Jô', 'Edu', 'João', 'Carlos', 'Joaquina']
# saída print: O valor na posição  5  é  ['Maria', 'Gui', 'Jô', 'Edu', 'João', 'Carlos', 'Joaquina']
# saída print: O valor na posição  6  é  ['Maria', 'Gui', 'Jô', 'Edu', 'João', 'Carlos', 'Joaquina']
# saída print: O valor na posição  7  é  ['Maria', 'Gui', 'Jô', 'Edu', 'João', 'Carlos', 'Joaquina']
# saída print: Valores nos vetores reais são:  [1.2, 3.5, 12.3, 4.2]