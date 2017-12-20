#this game is similar to space invaders
#you move your spaceship around using the arrow keys and shoot "w" for the left gin and "e" for the right gun
#your goal is to shoot as many asteroids before your ship is destroyed by the asteroids
#created by: Ryan Kinney

from graphics import *
from math import *
from random import *

def main():
    print("Press the arrow keys to move the white circle, press 'q' to quit")

    window_size = 600
    canvas_size = 20

    win = GraphWin("Animation Example with Keyboard", window_size, window_size)
    win.setCoords(0, 0, canvas_size, canvas_size)
    win.setBackground("black")

    p1 = Point(9, 2)
    p2 = Point(10, 4)
    p3 = Point(11, 2)
    p4 = Point(10, 2.5)
    p5 = Point(7.15, 2.5)
    p6 = Point(12.75, 2.5)
    p7 = Point(7.15, 4)
    p8 = Point(7.55, 2.5)
    p9 = Point(12.75, 4)
    p10 = Point(12.3, 2.5)

    hull = Polygon(p1,p2, p3)
    leftwing = Polygon(p4, p5, p1)
    rightwing = Polygon(p4, p6, p3)
    leftgun = Polygon(p5, p7, p8)
    rightgun = Polygon(p6, p9, p10)

    hull.setFill("white")
    leftwing.setFill("white")
    rightwing.setFill("white")
    leftgun.setFill("white")
    rightgun.setFill("white")

    hull.draw(win)
    leftwing.draw(win)
    rightwing.draw(win)
    leftgun.draw(win)
    rightgun.draw(win)

    while True:
        key = win.getKey()

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

        hull.move(delta_x, delta_y)
        leftwing.move(delta_x, delta_y)
        rightwing.move(delta_x, delta_y)
        leftgun.move(delta_x, delta_y)
        rightgun.move(delta_x, delta_y)

        laser_shot = False

        if key == " ":
            shoot(win)
            laser_shot = True

        if laser_shot = True:
            laser.move(0, 0.5)

def shoot(win):

        left_laser = Circle(get_left_gun_point(win), .5)
        left_laser.setFill("red")
        left_laser.draw(win)

        right_lazer = Circle(get_right_gun_point(win), .5)
        right_lazer.setFill("red")
        right_lazer.draw(win)


def get_right_gun_point(win):
    right_gun_point = Point(12.75, 4)

    key = win.getKey()

    delta_x = 0
    delta_y = 0

    if key == "Up":
        delta_y += 1
    elif key == "Down":
        delta_y -= 1
    elif key == "Left":
        delta_x -= 1
    elif key == "Right":
        delta_x += 1

    right_gun_point.move(delta_x,delta_y)

    right_gun_point.getY()
    right_gun_point.getX()


def get_left_gun_point(win):
    left_gun_point = Point(7.15, 4)

    key = win.getKey()

    delta_x = 0
    delta_y = 0

    if key == "Up":
        delta_y += 1
    elif key == "Down":
        delta_y -= 1
    elif key == "Left":
        delta_x -= 1
    elif key == "Right":
        delta_x += 1

    left_gun_point.move(delta_x,delta_y)

    left_gun_point.getX()
    left_gun_point.getY()

def asteroids():
    print()

def collide():
    print()

main()
