import pytest  # type: ignore
import uuid  # para criar os ids da biblioteca padrão do python
from sqlite3 import Connection  # Importa Connection do sqlite3
from .participants_repository import ParticipantsRepository
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando
def test_registry_participant():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    emails_to_trip_repository = EmailsToInviteRepository(conn)

    participant_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "emails_to_invite_id": "email",
        "name": "Teste1"
    }

    participants_repository.registry_participant(participant_infos)

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando

def test_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants = participants_repository.find_participants_from_trip(trip_id)
    print(participants)
