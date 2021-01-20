
class Kingdom:
    def __init__(self, name, emblem):
        self.name = name
        self.emblem = emblem
    
    def __str__(self):
        return f"{self.name}"

ALL_KINGDOMS = {
    "SPACE" : Kingdom("SPACE" ,"GORILLA"),
    "LAND" : Kingdom("LAND", "PANDA"),
    "WATER" : Kingdom("WATER", "OCTOPUS"),
    "ICE" : Kingdom("ICE", "MAMMOTH"),
    "AIR" : Kingdom("AIR", "OWL"),
    "FIRE" : Kingdom("FIRE","DRAGON")
}