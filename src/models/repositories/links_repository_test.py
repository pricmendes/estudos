# type: ignore serve para ignorar o erro que o python não está entendendo o pytest
import pytest # type: ignore
import uuid # para criar os ids da biblioteca padrão do python
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    link_infos = {
        "id"    : link_id,
        "trip_id": trip_id,
        "link": "www.google.com",
        "title": "airbnb"
    }

    link_repository.registry_link(link_infos)

@pytest.mark.skip(reason = "interação com o banco") # ignora os testes para que não sejam feitos alterações no banco de dados // caso queira testar a funcionalidade direta no banco é só retirar esse comando
def test_find_link_from_trip():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    links = link_repository.find_link_from_trip(trip_id)
    
    assert isinstance(links, list) # isinstance = Retorna se um objeto é uma instância de uma classe ou de uma subclasse dela.
    assert isinstance(links[0], tuple)
    print()
    print(links)

