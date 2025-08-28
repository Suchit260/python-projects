class Pet:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def show_info(self):
        return(f"Name: {self.name}, Age: {self.age}")
    def speak(self):
        return("....")

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def show_info(self):
         return(f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}")
    def speak(self):
        return("woof")
    
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show_info(self):
        return f"Cat: {self.name}, Age: {self.age}, Color: {self.color}"

    def speak(self):
        return "Meow"


class Bird(Pet):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def show_info(self):
        fly_status = "can fly" if self.can_fly else "cannot fly"
        return f"Bird: {self.name}, Age: {self.age}, {fly_status}"

    def speak(self):
        return "Chirp"

class PetManager:
    def __init__(self):
        self.pets = []   # an empty list to store all pets

    def add_pet(self, pet):
        self.pets.append(pet)   # adds a Pet (Dog, Cat, Bird) to the list

    def show_all_pets(self):
        for pet in self.pets:
            print(pet.show_info(), "| Sound:", pet.speak())

            
manager = PetManager()
dog = Dog("Bruno", 3, "Labrador")
cat = Cat("Kitty", 2, "Black")
bird = Bird("Tweety", 1, True)

manager.add_pet(dog)
manager.add_pet(cat)
manager.add_pet(bird)

manager.show_all_pets()
