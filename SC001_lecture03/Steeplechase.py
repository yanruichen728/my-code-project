"""
File: Steeplechase.py
Name: TODO:閻瑞辰
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):

        if front_is_clear():
            move()
        else:
            jump()

def jump():
    up()
    down()
def turn_right():
    for i in range(3):
        turn_left()
def up():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    #面向東方#
def down():
    turn_right()
    #面向南方#
    while front_is_clear():
        move()
    turn_left()
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
