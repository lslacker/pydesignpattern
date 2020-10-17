
class Dog:
    """A simple dog class"""

    def __str__(self):
        return 'Dog'

    def speak(self):
        return 'woof'

class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """returns a Dog object"""
        return Dog()

    def get_food(self):
        """return a Dog Foot object"""
        return "Dog food"


class PetStore:
    """PetStore hourses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        """pet factory  is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the object returned by the Dog factory"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("our pet is '{}'".format(pet))
        print("our pet says '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))

class Cat:
    """A simple cat class"""
    def __str__(self):
        return 'Cat'

    def speak(self):
        return 'Meow!'


factory = DogFactory()

shop = PetStore(factory)

shop.show_pet()
