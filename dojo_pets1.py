from dojo_pets import Pet, Dog, Cat

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self

omen = Pet("Omen", "Dog", "shake", "WOOF")
cypher = Dog("Cypher", "Dog", "jump", "WOOF", "Rottweiler")
mark = Ninja("Strika", "Bob", omen, "Cookies", "Raw Liver")
airriel = Ninja("Airriel", "Lambson", cypher, "Bananas", "Chicken")
anara = Cat("Anara", "Cat", "plop", "MEOW", "siamese")
mitch = Ninja("Mitch", "Lambson", anara, "Catnip", "Wet Food")


mark.feed().walk().bathe()
print(omen.energy)
print(omen.health)

airriel.feed().walk().bathe()
print(cypher.energy)
print(cypher.health)

mitch.feed().walk().bathe()
print(anara.energy)
print(anara.health)