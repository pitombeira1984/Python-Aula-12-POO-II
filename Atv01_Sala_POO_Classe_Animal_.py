
class Animal:
    def __init__(self, name):
        self.name = name
    def fazerSom(self):
        pass

class Cachorro(Animal):
    def fazerSom(self):
        return "woof!"
    
class Gato(Animal):
    def fazerSom(self):
        return "Meow"

rex = Cachorro("Rex")
whiskers = Gato("Whiskers")

print(rex.name, "faz", rex.fazerSom())
print(whiskers.name, "faz", whiskers.fazerSom())