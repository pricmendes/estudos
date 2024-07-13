import pytest
import uuid
from sqlite3 import Connection
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando

def test_registry_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "Atividade Teste",
        "occurs_at": "2024-07-15 10:00:00"
    }

    activities_repository.registry_activity(activity_infos)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activities WHERE id = ?", (activity_infos["id"],))
    activity = cursor.fetchone()

    assert activity is not None
    assert activity[0] == activity_infos["id"]
    assert activity[1] == activity_infos["trip_id"]
    assert activity[2] == activity_infos["title"]
    assert activity[3] == activity_infos["occurs_at"]

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando

def test_find_by_trip_id():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "Atividade Teste 2",
        "occurs_at": "2024-07-16 14:00:00"
    }

    activities_repository.registry_activity(activity_infos)

    activities = activities_repository.find_by_trip_id(trip_id)

    assert len(activities) > 0
    found = False
    for activity in activities:
        if activity[0] == activity_infos["id"]:
            found = True
            assert activity[1] == activity_infos["trip_id"]
            assert activity[2] == activity_infos["title"]
            assert activity[3] == activity_infos["occurs_at"]
            break
    assert found

