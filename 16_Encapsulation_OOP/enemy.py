"""
Encapsulation:
It means bundling of data.

There three types of class attributes
1. Public class attribute: Even after initialization, it can be overwritten.

2. Protected class attribute: With single (_) underscore considered protected, while not strictly enforced by interpreter.

3. Private class attributes: In python we use (__) double underscore to make private class attributes.
Python also uses name mangling to make them harder to access directly from outside the class.
This is achieved by prefixing the class name to the variable name (e.g, _ClassName__name)
While it's not an absolute barrier, it discourages accidental access

In Encapsulation, we use Getter and Setter
Getter is used to get values.
Setter is used to set values.

-> Encapsulation helps keep related fields and methods together.
-> Makes our code cleaner and easier to read.
-> Provides more flexibility to our code, gives more reusability with our code.

TIP: Python supports Encapsulation, while it doesn't enforce access restrictions as strictly as some other languages like Java.
"""


class Enemy:
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy # make it private attribute
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepare for fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.__type_of_enemy} attack for {self.attack_damage} damange")

    def get_type_of_enemy(self):  # getter function
        print(self.__type_of_enemy)