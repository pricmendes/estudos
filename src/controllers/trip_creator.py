from typing import Dict # importa o dicionário
from src.drivers.email_sender import send_email
import uuid

class TripCreator:
    def __init__(self, trips_repository, emails_repository) -> None:
        self.__trips_repository = trips_repository
        self.__emails_repository = emails_repository
        
        
    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")
            
            trip_id = str(uuid.uuid4())
            trip_infos = { **body, "id": trip_id } # os dois ** servem para indicar que estamos retirando todos os elementos chaves e valores de um dicionário e passando para outro 
            
            self.__trips_repository.create_trip(trip_infos)
            
            if emails:
                for email in emails:
                    self.__emails_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4())
                    })

            send_email(
                [body["owner_email"]],
                f"http://localhost:3000/trips/{trip_id}/confirm"
            )
            return {
                "body": { "id": trip_id },
                "status_code": 201 # o status 201 significa "criado"
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception) },
                "status_code": 400 # o status 400 significa "Solicitação Incorreta"
            }
            
        
        