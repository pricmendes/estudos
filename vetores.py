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