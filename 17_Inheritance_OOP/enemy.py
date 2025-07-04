"""
Inheritance:
Process of acquiring properties from one class to other class.

EXAMPLE:
    Parent Class: Attribute 1, Attribute2, Attribute3, Method1, Method2
    Child Class: (All Attributes from Parent class), Attribute4, Attribute5, (All Methods from Parent class), Method3, Method4

# Method Overriding
Is when a child class has its own method which is already present in the parent class.

And when the child class doesn't have the same method, it will default the present class.


# Self vs Super
-> self is used to refer to the current object that is created or being instantiated.
-> While super is used to refer to the parent class.
-> self is used when there is a need to differentiate between the instance variables and parameters with the same name.
-> While super is used to call the super class methods and/or constructors.


TIP: Parent class also called as Super class
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
        return f"{self.__type_of_enemy} attack for {self.attack_damage} damange"

    def get_type_of_enemy(self):  # getter function
        return self.__type_of_enemy