from enemy import *

class Zombie(Enemy): # Zombie is a child class of Enemy

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Zombie",
                         health_points=health_points,
                         attack_damage=attack_damage)


    def talk(self):     # This method will over-ridden the method that parent class has.
        print("*Grumbling...*") #Eample of over ridden when we call talk() this method will call not the parent method.


    def spread_disease(self):
        return "The Zombie is trying to spead infection."
