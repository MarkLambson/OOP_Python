class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 100
        self.energy = 50

    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.sound)

class Dog(Pet):
    def __init__(self, name, type, tricks, sound, breed):
        super().__init__(name, type, tricks, sound)
        self.breed = breed

class Cat(Pet):
    def __init__(self, name, type, tricks, sound, breed):
        super().__init__(name, type, tricks, sound)
        self.breed = breed