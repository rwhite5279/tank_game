#!/usr/bin/env python3
"""
game.py
"""

import random

def main():
    print("PLAY THE NUMBER GUESSING GAME! IT'S THE WORST!")
    n = int(random.randrange(3) + 1)
    g = int(input("Guess a number 1-3: "))
    if n == g:
        print("You guessed it!")
    else:
        print("Sorry, the number was " + str(n))
    
if __name__ == "__main__":
    main()
