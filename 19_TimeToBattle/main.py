from zombie import *
from ogre import *

# Both Zombie and Ogre are Enemy

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e1.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print("-"*12)
        e1.sepcial_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")
        e2.attack()
        e1.health_points = e1.health_points - e2.attack_damage
        e1.attack()
        e2.health_points = e2.health_points = e1.attack_damage

    print("-"*12)

    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')



zombie = Zombie(10, 1)
ogre = Ogre(20, 3)


battle(zombie, ogre)
