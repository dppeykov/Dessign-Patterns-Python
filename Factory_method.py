class Dog:

    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:

    """A simple cat class"""

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """The factory method"""

    # creates an instance of the dog or cat classes, based on the pet argument
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    # takes the pet from the pets dictionary, based on the argument
    return pets[pet]


d = get_pet("dog")

print(d.speak())  # Woof!

c = get_pet("cat")

print(c.speak())  # Meow!
