from enemy import *

# zombie = Enemy()
# Enemy() by default calling a constructor, called as empty constructor and python does it automatically when we are creating class.

# zombie.type_of_enemy = "Zombie"
# zombie.health_points = 21
# zombie.attack_damage = 10
#
# print(zombie.health_points)
# this technically works, but this not an ideal way to do it,
# the ideal way to do it by parameter constructor so while initiating an object we can give values to this class attributes.

"""
The above code is for Empty and No Argument Constructor
"""

zombie = Enemy('Zombie', 10, 1)
# This is the way to use parameter constructor, and good practice
big_zombie = Enemy("Big Zombie", 10, 100)

print(zombie.attack_damage)

print(big_zombie.attack_damage)


# But even in this if user can change some attribute values from here then he can

zombie2 = Enemy('Zombie', 10, 1)
zombie2.type_of_enemy = "Monster"

print(zombie2.type_of_enemy) # it will give Monster, instead of Zombie and that is not good, for fixing this we have Encapsulation. Shown in the next 16_Encapsulation_OOP