from typing import Dict # importa o dicionário
import uuid

class TripCreator:
    def __init__(self, trip_repository, emails_repository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository
        
        
    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")
            
            trip_id = str(uuid.uuid4())
            trip_infos = { **body, "id": trip_id } # os dois ** servem para indicar que estamos retirando todos os elementos chaves e valores de um dicionário e passando para outro 
            
            self.__trip_repository.create_trip(trip_infos)
            
            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4())
                    })
            return {
                "body": { "id": trip_id },
                "status_code": 201 # o status 201 significa "criado"
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400 # o status 400 significa "Solicitação Incorreta"
            }
            
        
        