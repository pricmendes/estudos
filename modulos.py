print("\n*-*-*-*-* Exemplo de importação de módulo padrão: *-*-*-*-*\n")
import math # Opção 1 de importação caso necessite de várias bibliotecas
from math import sqrt # Opção 2 de importação da função específica - melhor prática pois se houver alteração em várias funções de alguma atualização pode dar algum erro no programa


raiz_quadrada = int(math.sqrt(25))
print(f"A raiz quadrada do número 25 é: {raiz_quadrada}\n")

raiz_quadrada2 = int(sqrt(36))
print(f"A raiz quadrada do número 36 é: {raiz_quadrada2}\n")

print("Exemplo de criação e utilização de um módulo personalizado\n")

import meu_modulo # Opção de importar toda a biblioteca
from meu_modulo import saudacao, dobro # Opção de importar somente a função a ser utilizada

mensagem = meu_modulo.saudacao("Priscila")
resultado_dobro = meu_modulo.dobro(5)

print(mensagem)
print(f"\nO dobro de 5 é: {resultado_dobro}\n")
