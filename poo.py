# Linguagem de Programação Orientada a Objetos
# Conceitos - Suporte nativo
# Organização dos Programas em torno de Objetos (instâncias de classes)

# Exemplos de Classes e Objetos

# Classes
class Pessoa: # descrever atributos e métodos (ações)
    def __init__(self, nome, idade) -> None: # método init - self é uma refrência ao seu próprio objeto - uma porta de acesso para utilizar os métodos e atributos dessa classe - -> None signigica que não tem retorno
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Objetos - instâncias concretas da classe
pessoa1 = Pessoa("Priscila", 40) # armazenando os dados do objeto
# print("Nome:", pessoa1.nome)
# print("Idade:", pessoa1.idade)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome = "Rodrigo", idade = 32) # armazenando os dados do objeto
mensagem = pessoa2.saudacao()
print(mensagem)


# *** Pilares da POO Conceitos ***
# *** Herança ***
print("\nExemplo de Herança:")
# classe mãe:
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    def andar(self):
        print("O animal {self.nome} andou.")
        return
    def emitir_som(self):
        pass # pass instrução vazia
# classe filha herda os atributos da classe mãe
class Cachorro(Animal):
    def emitir_som(self):
        return "Au, Au!"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"


# *** Polimorfismo ***
# também herda da classe mãe porém é possível implementar ações diferentes
dog = Cachorro(nome = "Rex")
cat = Gato(nome = "Felix")

print("\nExemplo de Polimorfismo:\n")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}\n")


# *** Encapsulamento ***
print("\nExemplo de encapsulamento:\n")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # colocando dois __ o atributo irá se tornar privado, somente essa classe terá acesso a este atributo, somente os métodos dentro da classe terão acesso

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consulta_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo = 1000)
print(f"Saldo da conta bancária: {conta.consulta_saldo()}")

conta.depositar(valor = 500)
print(f"Saldo da conta bancária: {conta.consulta_saldo()}")

conta.depositar(valor = 800)
print(f"Saldo da conta bancária: {conta.consulta_saldo()}")

conta.sacar(valor = 400)
print(f"Saldo da conta bancária: {conta.consulta_saldo()}\n")

conta_do_zezinho = ContaBancaria(saldo = 50)
    

# *** Abstração ***
# Não possui capacidade de criar objetos diretamente dela
# Serve para molde de outras classes - protege as características

print("Exemplo de Abstração:\n")
from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod # decorador - definir que a classe é abstrata
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return ("Carro ligado usando a chave.")
    
    def desligar(self):
        return ("Carro desligou usando a chave.\n")

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())

# banco de dados - é necessário criar uma classe abstrata - em caso de mudança do banco você cria uma classe derivada do outro tipo de banco e você não precisa mudar as outras aplicações, somente da classe abstrata

# *** Herança múltipla ***
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando.\n"
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando.\n"

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        # super().emitir_som() serve para chamar a classe mãe e mostrar o que ela faz
        return "Morcegos emitem sons ultrassônicos.\n"
    
morcego = Morcego(nome = "Batman")

# Acessando métodos da classe base Animal
print("\nNome do morcego:", morcego.nome)
print("\nSom do morcego:", morcego.emitir_som())

# Acessando métodos das classes Mamígero e Ave
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())


# *** Decoradores ** permite modificar o comportamento de funções e métodos
from typing import Any
def meu_decorador(func): # func é a função que queremos exectuar 
    def wrapper(): # wrapper - embrulha em volta da função que queremos executar
        print("Antes da função ser chamada.\n")
        func()
        print("Depois da função ser chamada.\n")
    return wrapper

@meu_decorador # é o decoradaor que chama a função - 
def minha_funcao():
    print("Minha função foi chamada.\n")

minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        print("Antes da função ser chamada (decorador de classe)\n")
        self.func()
        print("Depois da função ser chamada (decorador de classe).\n")

@MeuDecoradorDeClasse    
def segunda_funcao():
    print("Segunda função foi chamada.\n")

segunda_funcao()

# *** Decoradores Comuns ***

class MinhaClasse:
    valor = 10 # Atributo da classe

    def __init__(self, nome) -> None:
        self.nome = nome # Atributo da instância

    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}.\n"
    
    @classmethod
    def metodo_classe(cls): # cls - classe
        return f"Método de classe chamado para valor = {cls.valor}.\n"

    @staticmethod
    def metodo_estatico(): # método estático não recebe nenhum argumento, ele não tem acesso aos atributos da classe nem da instância, mas ele pode executar uma função específica
        return f"Método estático chamado.\n"

obj = MinhaClasse(nome = "Classe exemplo")
print(obj.metodo_instancia())
# print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
configuracao1 = "Toyota, Corolla, 2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}\n")

class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b
    
print(Matematica.somar(a = 10, b = 15))
# Obs. não é uma boa prática que fica-se criando muitos métodos estáticos



