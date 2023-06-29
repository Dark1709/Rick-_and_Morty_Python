class Character ():
    def __init__(self, name: str, status: str, species: str, gender: str, origin: str):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        
    def __str__(self):
        return f"Name: {self.name}\nStatus: {self.status}\nSpecies: {self.species}\nGender: {self.gender}\nOrigin: {self.origin}"
    
""" celeste = Character("Celeste", "Vivo", "Humano", "Femenino", "Tierra")

print(celeste)
print(celeste.name)
print(celeste.status)
print(celeste.species)
print(celeste.gender)
print(celeste.origin) """

