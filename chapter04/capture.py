# animate_with_keys.py
#
# This program illustrates how to animate a drawing using input from the keyboard.
#
# by Mr. Ciccolo

from graphics import *
from random import *
from math import *

def main():
    print("Press the arrow keys to move the white circle, press 'q' to quit")

    score = 0
    timer = 60
    window_size = 600
    bounds = 20

    win = GraphWin("Animation Example with Keyboard", window_size, window_size)
    win.setCoords(0, 0, bounds, bounds)
    win.setBackground("black")

    timer_text = Text(Point(17,18), "Timer:")
    timer_text.setTextColor("white")
    timer_text.setFace("courier")
    timer_text.setSize(24)
    timer_text.draw(win)

    score_text = Text(Point(2,18), "Score:")
    score_text.setTextColor("white")
    score_text.setFace("courier")
    score_text.setSize(24)
    score_text.draw(win)

    circle = Circle(Point(bounds / 2, bounds / 2), 2)
    circle.setFill("white")
    circle.draw(win)

    pellet = Circle(Point(0, 0), 1)
    pellet.setFill("yellow")
    pellet.draw(win)
    collide(circle, pellet)
    move_to_random_point(pellet, bounds)

    time_check = time.time()

    while timer > 0:
        key = win.checkKey()

        delta_x = 0
        delta_y = 0

        if key == "q":
            break
        elif key == "Up":
            delta_y += 1
        elif key == "Down":
            delta_y -= 1
        elif key == "Left":
            delta_x -= 1
        elif key == "Right":
            delta_x += 1

        circle.move(delta_x, delta_y)

        if collide(circle,pellet):
            move_to_random_point(pellet,bounds)
            score += 1
            score_text.setText("Score:" + str(score))

        if time.time() - time_check > 1:
            timer -= 1
            time_check = time.time()
            timer_text.setText("Timer:" + str(timer))

    while timer < 1:
        endgame = Text(Point(10,10), "Game Over Press Q to quite")
        endgame.setTextColor("red")
        endgame.setFace("courier")
        endgame.setSize(24)
        endgame.draw(win)

        key=win.checkKey()

        if key == "q":
            break

def collide(c1, c2):
    a = c1.getCenter().getX() - c2.getCenter().getX()
    b = c1.getCenter().getY() - c2.getCenter().getY()

    c = sqrt(a**2 + b**2)

    return c <= (c1.getRadius() + c2.getRadius())

def move_to_random_point(circle, bounds):
    next_x = randrange(circle.getRadius(),bounds+1-circle.getRadius())
    next_y = randrange(circle.getRadius(),bounds+1-circle.getRadius())

    current_x = circle.getCenter().getX()
    current_y = circle.getCenter().getY()

    delta_x = next_x - current_x
    delta_y = next_y - current_y

    circle.move(delta_x, delta_y)

main()



