from typing import Dict, Tuple # permite especificar o tipo de dado  que cada elemento deve conter na coleção - retorna que é o modo tupla
from sqlite3 import Connection
from datetime import datetime, timezone
import sqlite3

# Registrar adaptadores personalizados para datetime
sqlite3.register_adapter(datetime, lambda dt: dt.isoformat())
sqlite3.register_converter('timestamp', lambda s: datetime.fromisoformat(s.decode('utf-8')).replace(tzinfo=timezone.utc))

class TripsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn # agora conseguimos usar a conexão do banco de dados com o um atributo da nossa classe

    def create_trip(self, trip_infos: Dict) -> None:
        cursor = self.__conn.cursor() # pega a conexão e tira um cursor da nossa conexão
        cursor.execute( # aspas triplas servem para possibilitar colocar uma string de sql com espaçamento de dar uma linha a mais 
            ''' 
                INSERT INTO trips
                    (id, destination, start_date, end_date, owner_name, owner_email)
                VALUES
                    (?, ?, ?, ?, ?, ?)
            ''', (
                trip_infos["id"],
                trip_infos["destination"],
                trip_infos["start_date"],
                trip_infos["end_date"],
                trip_infos["owner_name"],
                trip_infos["owner_email"]
            )
        )
        self.__conn.commit() # executa com o cursor acima e depois comita com esse comando
# buscando elementos no nosso banco de dados
    def find_trip_by_id(self, trip_id: str) -> Tuple: # id como string / e demonstra que o retorno é uma Tupla
        cursor = self.__conn.cursor() # é o cursor que mexe no nosso banco
        cursor.execute(
            ''' 
                SELECT * FROM trips WHERE id = ?
            ''', 
            (trip_id,) # id da viagem
            
        )
        trip = cursor.fetchone() # fetchone busca apenas 1 elemento no nosso banco - fetchmany ou fetchall busca vários elementos
        return trip # seleciona uma viagem através do id da viagem
    
    # será feito a atualização no campo status
    def update_trip_status(self, trip_id: str) -> None:
        cursor = self.__conn.cursor() # é o cursor que mexe no nosso banco
        cursor.execute(
            ''' 
                UPDATE trips 
                    SET status = 1
                WHERE
                    id = ?
            ''', 
            (trip_id,) # id da viagem
            
        )
        self.__conn.commit()
        
        

    