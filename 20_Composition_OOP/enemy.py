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

    def sepcial_attack(self):
        print("Enemy has no special attack.")