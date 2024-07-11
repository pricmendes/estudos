# type: ignore serve para ignorar o erro que o python não está entendendo o pytest
import pytest # type: ignore
import uuid # para criar os ids da biblioteca padrão do python
from datetime import datetime, timedelta # biblioteca para adicionar e subtrair dias
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

# criando a função para utilizar o pytest
db_connection_handler.connect() # conecta ao banco de dados
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando
def test_crate_trip():
    conn = db_connection_handler.get_connection() # pega a conexão
    trips_repository = TripsRepository(conn) # objeto instancia da nossa classe tripsrepository com a nossa conexão e fica armazenado como uma propriedade

    # criando dados ficticios - cadastrando uma viagem
    trips_infos = {
        "id": trip_id,
        "destination": "Barueri", # cidade da viagem
        "start_date": datetime.strptime("22-07-2024", "%d-%m-%Y"), # %d-$m-%Y indicam dia mês e ano
        "end_date": datetime.strptime("22-07-2024", "%d-%m-%Y") + timedelta(days = 8), # indica que irá adicionar + 8 dias para esta data que será a data final da viagem
        "owner_name": "Priscila", # pessoa que está organizando a viagem
        "owner_email": "priscila@email.com" # email da pessoa
    }

    trips_repository.create_trip(trips_infos) # enviando as informações do trips_infos para dentro - após isso pode rodar o pytest

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando
# testar o método find_trip_by_id - buscando a viagem e imprimindo ela na tela terminal
def test_find_trip_by_id(): 
    conn = db_connection_handler.get_connection() 
    trips_repository = TripsRepository(conn)

    # os registros são modo TUPLA caso queira pode ser selecionado o número do elemento na tupla

    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando
def test_update_trip_status(): 
    conn = db_connection_handler.get_connection() 
    trips_repository = TripsRepository(conn)

    # será feito a atualização no campo status

    trip = trips_repository.update_trip_status(trip_id) 
    print()
    print()
    print(trip)
    print()
    print()
















class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn # agora conseguimos usar a conexão do banco de dados com o um atributo da nossa classe

    def registry_participant(self, participant_infos: Dict) -> None:
        cursor = self.__conn.cursor() # pega a conexão e tira um cursor da nossa conexão
        cursor.execute( # aspas triplas servem para possibilitar colocar uma string de sql com espaçamento de dar uma linha a mais 
            '''
                INSERT INTO participants
                    (id, trip_id, emails_to_invite_id, name)
                VALUES
                ""  (?, ?, ?, ?, ?)

            ''', (
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["emails_to_invite_id"],
                participant_infos["name"]
                )
        )
        self.__conn.commit()

    def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT p.id, p.name, p.is_confirmed, e.email
                from participants as p
                JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id
                WHERE p.trip.id = ?
            ''', (trip_id,)
        )
        participants = cursor.fetchall()
        return participants
    
    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
               UPDATE participants
                    SET is_confirmed = 1
                WHERE 
                    id = ? 
            ''', (participant_id,)
            
        )