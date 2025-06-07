# Python Lista de Tarefas e Outros estudos:

Contém exemplos de código e módulos que abordam diversas funcionalidades e conceitos da linguagem Python, e uma lista de tarefas simples.

## Estrutura das Pastas e Arquivos:

- **[spamSimNao.py](https://github.com/pricmendes/estudosPython/blob/lista_tarefas_e_outros/spamSimNao.py)**  
  Exemplo de aprendizado de máquina. Demonstra o uso do aprendizado de máquina para classificar emails como spam.

- **[excecoes.py](https://github.com/pricmendes/estudosPython/blob/lista_tarefas_e_outros/excecoes.py)**  
  Exemplo de captura de exceções em Python. Demonstra o uso dos blocos `try`, `except`, `else`, e `finally` para tratamento de erros.

- **[meu_modulo.py](https://github.com/pricmendes/estudosPython/blob/lista_tarefas_e_outros/meu_modulo.py)**  
  Módulo personalizado com funções básicas:
  - `saudacao(nome)`: Retorna uma mensagem de saudação.
  - `dobro(numero)`: Retorna o dobro do número fornecido.

- **[modulo_terceiro.py](https://github.com/pricmendes/estudosPython/blob/lista_tarefas_e_outros/modulo_terceiro.py)**  
  Exemplo de importação e uso de um módulo de terceiros. Utiliza a biblioteca `requests` para realizar uma solicitação HTTP.

- **[modulos.py](https://github.com/pricmendes/estudosPython/blob/lista_tarefas_e_outros/modulos.py)**  
  Exemplo de importação de módulos padrão e personalizados:
  - Utiliza `math` e `sqrt` para operações matemáticas.
  - Demonstra a criação e uso de um módulo personalizado (`meu_modulo`).

- **[sintaxes.py](https://github.com/pricmendes/estudosPython/blob/lista_tarefas_e_outros/sintaxes.py)**  
  Exemplos de diferentes sintaxes e estruturas de dados em Python:
  - **Comentários**: Um e múltiplas linhas.
  - **Operadores de Strings**: Concatenação e formatação.
  - **Condicionais**: Uso de `if`, `elif`, e `else`.
  - **Listas**: Criação, manipulação e métodos.
  - **Tuplas**: Criação e métodos.
  - **Dicionários**: Criação, manipulação e métodos.
  - **Loops**: Exemplos de `for` e `while`, uso de `range` e `enumerate`.

- **[poo.py](https://github.com/pricmendes/estudosPython/blob/lista_tarefas_e_outros/poo.py)**  
  Exemplos de Programação Orientada a Objetos (POO) em Python, abordando os conceitos fundamentais como classes, objetos, herança, polimorfismo, encapsulamento, abstração, herança múltipla e decoradores. Inclui exemplos práticos de cada conceito.

- **[jogo](https://github.com/pricmendes/estudosPython/tree/lista_tarefas_e_outros/jogo)**  
  - *[jogo.py](https://github.com/pricmendes/estudosPython/blob/lista_tarefas_e_outros/jogo/jogo.py)*  
  Exemplo de um jogo de batalha simples em Python utilizando conceitos de Programação Orientada a Objetos. Inclui classes para heróis e inimigos, com métodos para ataque e defesa.

# Gerenciador de Tarefas:

- **[lista_tarefas](https://github.com/pricmendes/estudosPython/tree/lista_tarefas_e_outros/lista_tarefas)**  
  - *[gerenciador.py](https://github.com/pricmendes/estudosPython/blob/lista_tarefas_e_outros/lista_tarefas/gerenciador.py)*

Este é um simples gerenciador de tarefas em Python que permite adicionar, visualizar, atualizar, completar e deletar tarefas. Gerencia uma lista de tarefas com funcionalidades básicas de CRUD (Create, Read, Update, Delete).

## Funcionalidades:

1. **Adicionar Tarefa**: Adiciona uma nova tarefa à lista. A tarefa começa com o status de "não completada".
2. **Visualizar Tarefas**: Exibe a lista de tarefas com o status atual de cada uma.
3. **Atualizar Tarefa**: Permite alterar o nome de uma tarefa existente.
4. **Completar Tarefa**: Marca uma tarefa como completada.
5. **Deletar Tarefa**: Remove uma tarefa da lista, mas somente se a tarefa estiver marcada como completada.
6. **Sair**: Encerra o programa.
