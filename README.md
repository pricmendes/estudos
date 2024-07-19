# Projeto E-commerce API

Gerenciamento de um e-commerce, com funcionalidades para produtos e carrinho, e armazenamento de dados em um banco de dados SQLite.

## Estrutura do Projeto

- **[instance](https://github.com/pricmendes/estudosPython/tree/ecommerce/instance)**  
  Contém o banco de dados SQLite.  
  - *[ecommerce.db](https://github.com/pricmendes/estudosPython/blob/ecommerce/instance/ecommerce.db)*: Banco de dados para armazenar as informações do e-commerce.

- **[application.py](https://github.com/pricmendes/estudosPython/blob/ecommerce/application.py)**  
  Arquivo principal da aplicação contendo as rotas e endpoints.

- **[requirements.txt](https://github.com/pricmendes/estudosPython/blob/ecommerce/requirements.txt)**  
  Arquivo contendo as dependências do projeto.

- **[.gitignore](https://github.com/pricmendes/estudosPython/blob/ecommerce/.gitignore)**  
  Arquivo para ignorar arquivos e pastas no controle de versão.

## Funcionalidades

- **Gerenciamento de Produtos**  
  - Adicionar, editar, buscar e remover produtos do e-commerce.
  - Consultar detalhes de um produto específico.
  - Listar todos os produtos disponíveis.

- **Gerenciamento de Carrinho**  
  - Adicionar produtos ao carrinho.
  - Remover produtos do carrinho.
  - Visualizar itens no carrinho.
  - Realizar checkout e limpar o carrinho.

## Estrutura do Banco de Dados

O banco de dados SQLite (`ecommerce.db`) possui três tabelas:

1. **User**  
   - `id`: Identificador do usuário.
   - `username`: Nome de usuário.
   - `password`: Senha do usuário.

2. **Product**  
   - `id`: Identificador do produto.
   - `name`: Nome do produto.
   - `price`: Preço do produto.
   - `description`: Descrição do produto.

3. **CartItem**  
   - `id`: Identificador do item do carrinho.
   - `user_id`: Referência ao usuário dono do carrinho.
   - `product_id`: Referência ao produto adicionado ao carrinho.

## Observações

- A aplicação é construída em Flask e as rotas e endpoints são definidos no arquivo `application.py`.
- A autenticação é gerenciada com Flask-Login.
- O projeto está hospedado na AWS e pode ser acessado através do seguinte link: [http://api-ecommerce-dev.eba-wxb2vvjw.us-east-1.elasticbeanstalk.com](http://api-ecommerce-dev.eba-wxb2vvjw.us-east-1.elasticbeanstalk.com). 
- Em algum momento a aplicação não ficará disponível mais na AWS devido custos.
