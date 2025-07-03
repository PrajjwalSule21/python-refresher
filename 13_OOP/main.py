from enemy import *

enemy1 = Enemy()
enemy2 = Enemy()
enemy2.health_points = 100
enemy2.attack_damage = 21

enemy1.type_of_enemy = "Zombie"
enemy2.type_of_enemy = "Monster"

print(enemy1.health_points)
print(enemy2.health_points)


print(f"{enemy1.type_of_enemy} has {enemy1.health_points} health points and can do"
      f"an attack of {enemy1.attack_damage} damage")

print(f"{enemy2.type_of_enemy} has {enemy2.health_points} health points"
      f"and can do an attack of {enemy2.attack_damage} damage")
