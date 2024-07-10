meu_dicionario = {
    "Olá": "Mundo!",
    "estou": "aqui"
}

outro_dicionario = {
    **meu_dicionario,
    "Teste": "testando dicionários",
    "aqui": "meu dicionário"
}
print()
print(outro_dicionario)
print()

# resultado na tela será {'Olá': 'Mundo!', 'estou': 'aqui', 'Teste': 'testando dicionários', 'aqui': 'meu dicionário'}
# ou seja ele concatenou os dois dicionários