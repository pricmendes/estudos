def delta(a, b, c):
	return(b ** 2 - 4 * a * c)

def equacao(a,b,c):
	
	resultadoDelta = delta(a, b, c)
	print("Delta calculado: {}".format(resultadoDelta))
	if resultadoDelta < 0:
		return "Não possui resultados reais"
	else:
		print("Delta: {}".format(resultadoDelta))

	x1 = (((-1) * b) + (resultadoDelta ** (1 / 2))) / (2 * a)

	x2 = (((-1) * b) - (resultadoDelta ** (1 / 2))) / (2 * a)

	return f"Os resultados possíveis são \nX1: {x1:.0f}\nX2: {x2:.0f}"

def main():

	print("Cálculo da equação do 2º grau\n ax² + bx + c = 0")
	print("\n")

	try:

		valorA = int(input("Informe o valor de 'a':"))

		valorB = int(input("Informe o valor de 'b':"))

		valorC = int(input("Informe o valor de 'c':"))

		print(equacao(valorA, valorB, valorC))

	except ValueError as erro:

		print("O valor informado não é inteiro")

main()


# saída print: Cálculo da equação do 2º grau
# saída print:  ax² + bx + c = 0
# saída print: 
# saída print: 
# saída print: Informe o valor de 'a':6
# saída print: Informe o valor de 'b':8
# saída print: Informe o valor de 'c':10
# saída print: Delta calculado: -176
# saída print: Não possui resultados reais