print("\nExemplo de captura de exceções.\n")

try:

    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("\nTipo de variáveis incompatíveis. Entre com um número inteiro.\n")
except Exception as e:
    print(f"Erro: {e}")    
else:
    print(f"\nResultado: {resultado} \n")
finally:
    print("\nOperação Finalizada.\n")




