"""
File: PotholeFilling.py
Name: TODO:閻瑞辰
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *
def turn_right():
    for i in range(3):
        turn_left()


def go_in():
    move()
    turn_right()
    move()
    put_a_lot()
def go_out():
    turn_left()
    turn_left()
    move()
    turn_right()
    move()


def put_a_lot():
    for i in range(99):
        put_beeper()
def main():
    """
    TODO:閻瑞辰
    """

    pass
    go_in()
    go_out()
    go_in()
    go_out()
    go_in()
    go_out()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
