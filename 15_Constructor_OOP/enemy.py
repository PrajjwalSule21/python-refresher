"""
Constructor:
Are used to create and initialize an object of a class with or without storing values.

1. Default/Empty Constructors
2. No Arguments Constructors
3. Parameters Constructors
"""


class Enemy:
    # type_of_enemy: str
    # health_points: int = 10
    # attack_damage: int = 1

    """
    Python by default create an empty constructor
    We don't need to write this code
    """
    # def __init__(self):
    #     pass

    """
    This is the example of No argument constructor
    """
    # def __init__(self):
    #     print("This is Enemy!")

    """
    This is Parameter Constructor
    """

    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepare for fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attack for {self.attack_damage} damange")