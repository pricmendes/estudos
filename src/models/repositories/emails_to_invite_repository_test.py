# type: ignore serve para ignorar o erro que o python não está entendendo o pytest
import pytest # type: ignore
import uuid # para criar os ids da biblioteca padrão do python
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_trip_repository = EmailsToInviteRepository(conn)

    emails_trips_infos = {
        "id"    : str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olamundo@email.com"
    }

    emails_to_trip_repository.registry_email(emails_trips_infos)

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_trip_repository = EmailsToInviteRepository(conn)

    emails = emails_to_trip_repository.find_emails_from_trip(trip_id)
    print()
    print(emails)

