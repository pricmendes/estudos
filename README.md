# Projeto E-commerce API

Gerenciamento de um e-commerce, com funcionalidades para produtos, categorias e pedidos, e armazenamento de dados em um banco de dados SQLite.

## Estrutura do Projeto

- **[instance](https://github.com/pricmendes/estudosPython/tree/ecommerce/instance)**  
  Contém o banco de dados SQLite.  
  - *[ecommerce.db](https://github.com/pricmendes/estudosPython/blob/ecommerce/instance/ecommerce.db)*: Banco de dados para armazenar as informações do e-commerce.

- **[app.py](https://github.com/pricmendes/estudosPython/blob/ecommerce/app.py)**  
  Arquivo principal da aplicação contendo as rotas e endpoints.

- **[requirements.txt](https://github.com/pricmendes/estudosPython/blob/ecommerce/requirements.txt)**  
  Arquivo contendo as dependências do projeto.

- **[.gitignore](https://github.com/pricmendes/estudosPython/blob/ecommerce/.gitignore)**  
  Arquivo para ignorar arquivos e pastas no controle de versão.

## Funcionalidades

- **Gerenciamento de Produtos**  
  Adicionar, editar, buscar e remover produtos do e-commerce.

- **Gerenciamento de Categorias**  
  Adicionar, editar, buscar e remover categorias de produtos.

- **Gerenciamento de Pedidos**  
  Criar, buscar e atualizar status de pedidos realizados no e-commerce.

## Observações

- O projeto utiliza um banco de dados SQLite (`ecommerce.db`) para armazenar as informações.
- A aplicação é construída em Flask e as rotas e endpoints são definidos no arquivo `app.py`.
