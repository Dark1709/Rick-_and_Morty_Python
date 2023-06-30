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

        if response.status_code == 200:
            character = response.json()
            return self.__from_response_to_character(character)
        else:
            return "No se encontró el personaje"
        

    def get_multiple_characters(self, character_list: list):
        characters = []
        for character_id in character_list:
            character = self.get_character_by_id(character_id)
            characters.append({character})
        return characters
    
    
    def filter_character(self, character_id: int, attributes: list):
        character = self.get_character_by_id(character_id).__dict__
        filtered_character = {
            key: character[key] for key in character if key in attributes
        }
        return filtered_character
    
    
services = CharacterService()
attributes = ['name', 'status', 'species']
characters_list = [1,2,3,4,5]

character_group = services.get_multiple_characters(characters_list)
print(character_group)

character = services.get_character_by_id("1")
filtered_character = services.filter_character(5, attributes)
print(filtered_character)

print(character)