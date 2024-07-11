from typing import Dict, Tuple, List # permite especificar o tipo de dado  que cada elemento deve conter na coleção - retorna que é o modo tupla - retorna modo lista
from sqlite3 import Connection
import sqlite3

class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn # agora conseguimos usar a conexão do banco de dados com o um atributo da nossa classe

    def registry_activity(self, activity_infos: Dict) -> None:
        cursor = self.__conn.cursor() # pega a conexão e tira um cursor da nossa conexão
        cursor.execute( # aspas triplas servem para possibilitar colocar uma string de sql com espaçamento de dar uma linha a mais 
            ''' 
                INSERT INTO activities
                    (id, trip_id, title, occurs_at)
                VALUES
                    (?, ?, ?, ?)
            ''', (
                activity_infos["id"],
                activity_infos["trip_id"],
                activity_infos["title"],
                activity_infos["occurs_at"]
            )
        )
        self.__conn.commit() # executa com o cursor acima e depois comita com esse comando

# buscando elementos no nosso banco de dados
    def find_by_trip_id(self, trip_id: str) -> List[Tuple]: # id como string / e demonstra que o retorno é uma Lista de Tuplas
        cursor = self.__conn.cursor() # é o cursor que mexe no nosso banco
        cursor.execute(
            ''' 
                SELECT * FROM activities WHERE trip_id = ?
            ''', 
            (trip_id,) # id da viagem
            
        )
        activities = cursor.fetchall() # fetchone busca apenas 1 elemento no nosso banco - fetchmany ou fetchall busca vários elementos
        return activities # seleciona um email através do id da viagem


    