class Pilha2:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if self.elementos:
            return self.elementos.pop()
        else:
            return "Pilha vazia"

    def top(self):
        if self.elementos:
            return self.elementos[-1]
        else:
            return "Pilha vazia"


minha_pilha = Pilha2()
minha_pilha.push("Python")
minha_pilha.push("Java")
minha_pilha.pop()
minha_pilha.push("C++")

print(minha_pilha.top())  # Output: C++

