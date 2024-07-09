import sqlite3 # já vem com o Python
from sqlite3 import Connection

class DbConnectionHandler: # criação da classe
    def __init__(self) -> None: # método construtor um init para colocar os atributos da classe
        self.__connection_string = "storage.db" # string para conexão com nosso banco que está na raiz do nosso projeto (sqlite)
        self.__conn = None # o none irá mudar pois iremos armazenar a nossa conexão aqui

    def connect(self) -> None: # método para não retornar nada para o nosso usuário - conexão ao banco de dados
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False) # nossa string de conexão - check_same_thread=False caso queira utilizar a conexão em vários lugares do projeto a gente consegue utilizar tirando o false
        self.__conn = conn # deixa a conexão aqui que está associado ao atributo da classe acima

    def get_connection(self) -> Connection:
        return self.__conn # retorna um tipo conexão em sqlite
    
db_connection_handler = DbConnectionHandler() # para ter uma única conexão no projeto todo / improta o objeto que já tem a conexão direta com o banco
