"""
Abstraction:
This means to hide the implementation and only shows necessary details to the user.

Analogy: Flashlight, User only know when he turned on the switch the light is on,
and vice versa without knowing the internal functionality behind it

Why Abstraction is needed:
1. This allows users to not have to understand what the functionality is behind scenes.
2. You can create simple and reusable code.
3. Allows for a better use of the DRY (Don't Repeat Yourself)
4. Enables Python objects to become more scalable.
"""


class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepare for fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attack for {self.attack_damage} damange")