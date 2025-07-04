"""
Polymorphism:

Polymorphism means to have many forms.
One common way to see polymorphism in Python is through method overriding in inheritance. This is when a subclass provides its own specific implementation of a method that is already defined in its parent class. Even though the method has the same name, its behavior changes depending on the object's actual type.
We can also say that changing that object at a specific runtime

EXAMPLE:
    zoo: Animal = [] #Empty list

    class Dog(Animal):
        # all Dog methods

    class Bird(Animal):
        # all Bird methods


    dog = Dog()
    zoo.append(dog) -> This will work

    dog = Animal
    zoo.append(dog) -> This will also work
"""


class Enemy:
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy # make it private class attribute
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        return f"I am a {self.__type_of_enemy}. Be prepare for fight!"

    def walk_forward(self):
        return f"{self.__type_of_enemy} moves closer to you."

    def attack(self):
        print(f"{self.__type_of_enemy} attack for {self.attack_damage} damage")

    def get_type_of_enemy(self):  # getter function
        return self.__type_of_enemy