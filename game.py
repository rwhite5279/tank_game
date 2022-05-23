#!/usr/bin/env python3
"""
game.py
This Python3 program plays an "aggressive tank" game against
the computer.

May the best tank win!
"""

__author__ = "Richard White"
__version__ = "2022-05-23"

import random

def random_missile():
    n = int(random.randrange(3))
    if n == 0:
        return 1        # 1/3 chance of hitting!
    else:
        return 0        # 2/3 chance of missing

def main():
    print("PLAY THE AGGRESSIVE TANK GAME. TRY TO KILL YOUR ENEMY!")
    user = 3
    enemy = 3
    while (user > 0 and enemy > 0):
        input("Press [enter] to fire a missile at your enemy...")
        if random_missile() == 1:
            print("It's a hit!")
        else:
            print("You missed.")
        if enemy > 0:
            print("The enemy is firing at you...")
            if random_missile() == 1:
                print("You've been hit!")
                user -= 1
            else:
                print("They just missed you.")

    print("Game Over")
    
if __name__ == "__main__":
    main()
