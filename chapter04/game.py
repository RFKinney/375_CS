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
    p4 = Point(9.75, 2.5)
    p5 = Point(7.15, 2.5)
    p6 = Point(12.75, 2.5)

    hull = Polygon(p1,p2, p3)
    leftwing = Polygon(p4, p5, p1)
    rightwing = Polygon(p4, p6, p3)
    leftgun = Polygon()
    rightgun = Polygon()

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

main()
