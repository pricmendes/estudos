from typing import Dict

class ActivityFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def find_from_trip(self, trip_id: str) -> Dict:
        try: 
            activities = self.__activities_repository.find_by_trip_id(trip_id)
            
            formatted_activities = []
            for activity in activities:
                formatted_activities.append({
                    "id": activity[0],
                    "title": activity[2],
                    "occurs_at": activity[3]
                                    
                })
            return {
                "body": { "activities": formatted_activities},
                "status_code": 200 # tratamento de erros - 200 é bem sucedido 
                
            }
        except Exception as exception:
                return {
                    "body": { "error": "Bad Request", "message": str(exception) },
                    "status_code": 400 # o status 400 significa "Solicitação Incorreta"
                }


