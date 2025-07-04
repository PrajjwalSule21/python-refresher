from zombie import *
from ogre import *

zombie = Zombie(10, 1)


print(zombie.get_type_of_enemy())
print(zombie.talk())  # This call child method

print(zombie.spread_disease())


ogre = Ogre(20, 3)

print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points an can attack of {zombie.attack_damage}")
print(f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points an can attack of {ogre.attack_damage}")


print(ogre.talk()) # this will call the child method


# These will uses parent/super class method as we haven't over-ridden it in child.
print(zombie.walk_forward())
print(ogre.walk_forward())


print(zombie.attack())
print(ogre.attack())