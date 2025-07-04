from zombie import *
from ogre import *
from hero import *
from weapon import *


def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print("-"*21)

        enemy.special_attack()

        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP left")
        enemy.attack()
        hero.health_points = hero.health_points - enemy.attack_damage
        hero.attack()
        enemy.health_points = enemy.health_points - hero.attack_damage

    print("-"*21)

    if hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')



zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
hero = Hero(10,1)
weapon = Weapon("Sword", 10)
hero.weapon = weapon
hero.equip_weapon()


hero_battle(hero, zombie)
