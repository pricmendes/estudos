# Projeto Trip

Um projeto em Python usando Flask para gerenciar viagens, participantes, atividades e links, com funcionalidades de envio de e-mails.

## Estrutura do Projeto

- **.[vscode](https://github.com/pricmendes/estudosPython/tree/trip/.vscode)/**
  Contém configurações específicas do VSCode.  
  - *[settings.json](https://github.com/pricmendes/estudosPython/blob/trip/.vscode/settings.json)*: Configurações do editor.

- **[init](https://github.com/pricmendes/estudosPython/tree/trip/init)/**  
  Contém o script SQL para inicializar o banco de dados.  
  - *[schema.sql](https://github.com/pricmendes/estudosPython/blob/trip/init/schema.sql)*: Script para criar as tabelas e inserir dados iniciais.

- **[src](https://github.com/pricmendes/estudosPython/tree/trip/src)/**  
  Contém os principais componentes da aplicação.  
  - **[controllers](https://github.com/pricmendes/estudosPython/tree/trip/src/controllers)/**: Controladores que gerenciam a lógica de negócio.  
    - *[activity_creator.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/activity_creator.py)*: Criar atividades.  
    - *[activity_finder.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/activity_finder.py)*: Buscar atividades.  
    - *[link_creator.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/link_creator.py)*: Criar links.  
    - *[link_finder.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/link_finder.py)*: Buscar links.  
    - *[participant_confirmer.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/participant_confirmer.py)*: Confirmar participantes.  
    - *[participant_creator.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/participant_creator.py)*: Criar participantes.  
    - *[participant_finder.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/participant_finder.py)*: Buscar participantes.  
    - *[trip_confirmer.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/trip_confirmer.py)*: Confirmar viagens.  
    - *[trip_creator.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/trip_creator.py)*: Criar viagens.  
    - *[trip_finder.py](https://github.com/pricmendes/estudosPython/blob/trip/src/controllers/trip_finder.py)*: Buscar viagens.

  - **[drivers](https://github.com/pricmendes/estudosPython/tree/trip/src/drivers)/**: Contém drivers para funcionalidades específicas.  
    - *email_sender.py(https://github.com/pricmendes/estudosPython/blob/trip/src/drivers/email_sender.py)*: Driver para envio de e-mails.

  - **[routes](https://github.com/pricmendes/estudosPython/tree/trip/src/main/routes)/**: Definição das rotas da API.  
    - *[trips_routes.py](https://github.com/pricmendes/estudosPython/blob/trip/src/main/routes/trips_routes.py)*: Rotas relacionadas a viagens.

  - **[server](https://github.com/pricmendes/estudosPython/tree/trip/src/main/server)/**: Configuração do servidor Flask.  
    - *[server.py](https://github.com/pricmendes/estudosPython/blob/trip/src/main/server/server.py)*: Configuração principal do servidor.

  - **[models](https://github.com/pricmendes/estudosPython/tree/trip/src/models)/**: Modelos e repositórios para acesso ao banco de dados.  
    - **[repositories](https://github.com/pricmendes/estudosPython/tree/trip/src/models/repositories)/**: Repositórios que gerenciam a persistência dos dados.  
      - *[activities_repository.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/activities_repository.py)*: Repositório de atividades.  
      - *[activities_repository_test.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/activities_repository_test.py)*: Testes para o repositório de atividades.  
      - *[emails_to_invite_repository.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/emails_to_invite_repository.py)*: Repositório de e-mails a serem convidados.  
      - *[emails_to_invite_repository_test.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/emails_to_invite_repository_test.py)*: Testes para o repositório de e-mails a serem convidados.  
      - *[links_repository.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/links_repository.py)*: Repositório de links.  
      - *[links_repository_test.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/links_repository_test.py)*: Testes para o repositório de links.  
      - *[participants_repository.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/participants_repository.py)*: Repositório de participantes.  
      - *[participants_repository_test.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/participants_repository_test.py)*: Testes para o repositório de participantes.  
      - *[trips_repository.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/trips_repository.py)*: Repositório de viagens.  
      - *[trips_repository_test.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/repositories/trips_repository_test.py)*: Testes para o repositório de viagens.
      
    - **[settings](https://github.com/pricmendes/estudosPython/tree/trip/src/models/settings)/**: Configurações do banco de dados.  
      - *[db_connection_handler.py](https://github.com/pricmendes/estudosPython/blob/trip/src/models/settings/db_connection_handler.py)*: Manipulador de conexão com o banco de dados.

- **[.gitignore](https://github.com/pricmendes/estudosPython/blob/trip/.gitignore)**  
  Arquivo para ignorar arquivos e pastas no controle de versão.

- **[create_email.py](https://github.com/pricmendes/estudosPython/blob/trip/create_email.py)**  
  Script para criar uma conta de e-mail usando a API do Nodemailer.

- **[run.py](https://github.com/pricmendes/estudosPython/blob/trip/run.py)**  
  Script principal para rodar a aplicação.

- **[storage.db](https://github.com/pricmendes/estudosPython/blob/trip/storage.db)**  
  Banco de dados SQLite.

## Funcionalidades

- **Criação e Busca de Viagens**  
  Através de rotas e controladores específicos, o projeto permite criar e buscar informações sobre viagens.

- **Gerenciamento de Participantes**  
  Criação, busca e confirmação de participantes para as viagens.

- **Atividades**  
  Possibilidade de criar e buscar atividades associadas às viagens.

- **Links**  
  Criação e busca de links associados às viagens.

- **Envio de E-mails**  
  Uso do driver para envio de e-mails, incluindo a criação de contas de e-mail através do script `create_email.py`.

## Observações

- O projeto usa um banco de dados SQLite (`storage.db`) para armazenar as informações.
- O script `create_email.py` é utilizado para criar uma conta de e-mail no serviço Ethereal usando a biblioteca `requests`.
- A aplicação é construída em Flask.
