import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Criar um conjunto de dados manualmente
data = {
    'expressao_facial': [1, 2, 3, 4, 1],  # 1: Sorriso, 2: Neutra, 3: Tensa, 4: Irritada
    'tom_de_voz': [1, 1, 2, 3, 1],        # 1: Calmo, 2: Neutro, 3: Agressivo
    'postura': [1, 2, 3, 4, 1],           # 1: Relaxado, 2: Tenso, 3: Enérgico, 4: Fechado
    'humor': [1, 1, 0, 0, 1]              # 1: Bom, 0: Ruim
}

# 2. Converter o dicionário em um DataFrame
df = pd.DataFrame(data)

# 3. Dividir os dados em conjuntos de treino e teste
X = df.drop('humor', axis=1)  # X contém as características (expressão facial, tom de voz, postura)
y = df['humor']               # y contém as etiquetas (humor: 1 para bom, 0 para ruim)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Treinar o modelo de aprendizado de máquina
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Fazer previsões com o modelo treinado
y_pred = model.predict(X_test)

# 6. Calcular a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy:.2f}')

# 7. Testar o modelo com novos dados inseridos manualmente
novos_dados = {
    'expressao_facial': [2],  # Exemplo: 2 = Neutra
    'tom_de_voz': [3],        # Exemplo: 3 = Agressivo
    'postura': [4]            # Exemplo: 4 = Fechado
}

novos_dados_df = pd.DataFrame(novos_dados)
previsao = model.predict(novos_dados_df)
print(f'Previsão do humor: {"Bom" if previsao[0] == 1 else "Ruim"}')


# saida 
# Acurácia do modelo: 1.00
# Previsão do humor: Ruim
