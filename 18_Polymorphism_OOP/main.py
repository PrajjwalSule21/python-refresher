from zombie import *
from ogre import *

# Both Zombie and Ogre are Enemy

def battle(e: Enemy): #passing a generic type
    e.talk()
    e.attack()

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)


battle(zombie)
battle(ogre)