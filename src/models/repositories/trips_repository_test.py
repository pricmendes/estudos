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


