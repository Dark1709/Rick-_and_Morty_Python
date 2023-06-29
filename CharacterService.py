import requests
from Character import Character 


class CharacterService():
    def __init__(self):
        self.__BASE_URL = 'https://rickandmortyapi.com/api/character/'
        
    def __from_response_to_character(self, response: dict):
       
        return Character(
                name = response['name'],
                status = response['status'],
                species = response['species'],
                gender=response['gender'],
                origin=response['origin']['name']
            )
        
    def get_character_by_id(self, character_id: int)->Character:
        url = f"{self.__BASE_URL}{character_id}"
        response = requests.get(url)
        character = response.json()
        return self.__from_response_to_character(character)
    
services = CharacterService()
character = services.get_character_by_id(1)

print(character)