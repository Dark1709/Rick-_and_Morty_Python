from CharacterService import CharacterService


services = CharacterService()

character_id_input = input("Ingrese el ID del personaje que desea consultar: ")
character_id = int(character_id_input.strip())
character = services.get_character_by_id(character_id)
print("\nPersonaje:")
print(character)


characters_input = input("\nIngrese los IDs de los personajes separados por comas: ")
characters_list = [int(character_id.strip()) for character_id in characters_input.split(",")]

character_group = services.get_multiple_characters(characters_list)
print("\nGrupo de personajes:")
for character in character_group:
    print(character)

attributes_input = input("\nIngrese los atributos por los que desea filtrar separados por comas: ")
attributes = [attr.strip() for attr in attributes_input.split(",")]

character_id_input = input("\nIngrese el ID del personaje a filtrar: ")
character_id = int(character_id_input.strip())

filtered_character = services.filter_character(character_id, attributes)
if filtered_character:
    print("\nPersonaje filtrado:")
    print(filtered_character)
else:
    print(f"\nNo se encontró el personaje con ID {character_id}")
