import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 1. Coleta de Pistas: Carregar o conjunto de dados
# Exemplo fictício de dados. Quantos mais dados você incluir mais ele irá aprender a classificar como Spam.
data = {
    'email': [
        'Ganhe dinheiro rápido e fácil!',
        'Você ganhou um prêmio incrível!',
        'Olá, estou enviando o relatório solicitado.',
        'Você foi selecionado para um prêmio incrível!',
        'Aqui está o link para nossa reunião de amanhã.',
        'Compre agora e ganhe um desconto exclusivo!',
        'Lembrete: Reunião às 10h.'
    ],
    'spam': [1, 1, 0, 1, 0, 1, 0]  # 1: Spam, 0: Não spam
}

df = pd.DataFrame(data)

# 2. Processamento dos Dados
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['email'])  # Converte o texto em uma matriz de contagem de palavras
y = df['spam']  # Etiquetas (spam ou não spam)

# 3. Divisão dos Dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Treinamento do Modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# 5. Fazer Previsões
y_pred = model.predict(X_test)

# 6. Acurácia do Modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')

# 7. Testar com Novos E-mails
novos_emails = ['Você ganhou um carro novo!', 'Lembrete: Reunião às 10h.']
novos_emails_transformed = vectorizer.transform(novos_emails)
previsao = model.predict(novos_emails_transformed)

for i, email in enumerate(novos_emails):
    print(f'Email: "{email}" - Classificado como: {"Spam" if previsao[i] == 1 else "Não Spam"}')
    

# Modelo de Reconhecimento de Padrões para classificação de e-mails Spam Sim ou Não.

# Deve-se treinar o modelo com o máximo de informações possíveis para que ele possa classificar se o email é um Spam, por isso é importante informar Modelos de Mensagens e classificá-las como Spam (1) ou Não Spam (0).

# Utilizei a biblioteca Sklearn que é muito utilizada para aprendizado de máquina.

# Realizado o treinamento inicial.

# 1. Coleta de Pistas e carregamento do conjunto de dados.

# 2. Processamento dos Dados

# 3. Divisão dos Dados 

# 4. Treinamento do Modelo 

# 5. Fazer Previsões

# 6. Acurácia do Modelo para saber o quanto o modelo acertou a previsão

# 7. Testar com Novos E-mails

# CountVectorizer: Transforma o texto dos e-mails em uma matriz numérica, onde cada coluna representa uma palavra e cada linha um e-mail.
# MultinomialNB: Classifica o texto que será treinado nos dados de e-mails.
# Acurácia: Avalia se o modelo está classificando os e-mails com base no conjunto de teste.
# Novos E-mails: Testa o modelo com novos e-mails para ver como ele os classifica.

# Retorno:

# Acurácia do modelo: 1.00
# Email: "Você ganhou um carro novo!" - Classificado como: Spam
# Email: "Lembrete: Reunião às 10h." - Classificado como: Não Spam
