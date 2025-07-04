from enemy import *


zombie = Enemy('Zombie', 10, 1)

# print(zombie.__type_of_enemy) # Gives error: AttributeError: 'Enemy' object has no attribute '__type_of_enemy'

print(zombie.get_type_of_enemy()) # this will get the value: Zombie

# without getter, we can access that private class attribute by name mangling

# _ClassName__variable
print(zombie._Enemy__type_of_enemy) # this will give : Zombie


"""
getters are preferred for controlling access to attributes and providing encapsulation, 
while name mangling is useful for avoiding naming conflicts in inheritance hierarchies.
"""