from typing import Dict, Tuple, List # permite especificar o tipo de dado  que cada elemento deve conter na coleção - retorna que é o modo tupla - retorna modo lista
from sqlite3 import Connection
import sqlite3

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn # agora conseguimos usar a conexão do banco de dados com o um atributo da nossa classe

    def registry_link(self, links_infos: Dict) -> None:
        cursor = self.__conn.cursor() # pega a conexão e tira um cursor da nossa conexão
        cursor.execute( # aspas triplas servem para possibilitar colocar uma string de sql com espaçamento de dar uma linha a mais 
            ''' 
                INSERT INTO links
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                links_infos["id"],
                links_infos["trip_id"],
                links_infos["link"],
                links_infos["title"]
            )
        )
        self.__conn.commit() # executa com o cursor acima e depois comita com esse comando

# buscando elementos no nosso banco de dados
    def find_link_from_trip(self, trip_id: str) -> List[Tuple]: # id como string / e demonstra que o retorno é uma Lista de Tuplas
        cursor = self.__conn.cursor() # é o cursor que mexe no nosso banco
        cursor.execute(
            ''' 
                SELECT * FROM links WHERE trip_id = ?
            ''', 
            (trip_id,) # id da viagem
            
        )
        links = cursor.fetchall() # fetchone busca apenas 1 elemento no nosso banco - fetchmany ou fetchall busca vários elementos
        return links # seleciona um email através do id da viagem


    