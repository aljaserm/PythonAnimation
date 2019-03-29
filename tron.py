from random import randrange
from turtle import *
from base import square, vector

p1 = vector(-100, 0)
p1Aim = vector(4, 0)
p1Body = set()
p2 = vector(100, 0)
p2Aim = vector(-4, 0)
p2Body = set()


def inside(head):
    return -200 < head.x < 200 and -200 < head.y < 200


def draw():
    p1.move(p1Aim)
    p1Head = p1.copy()
    p2.move(p2Aim)
    p2Head = p1.copy()
    if not inside(p1Head) or p1Head in p2Body:
        print("Blue Won")
        return
    if not inside(p2Head) or p2Head in p1Body:
        print("Red Won")
        return
    p1Body.add(p1Head)
    p2Body.add(p2Head)
    square(p1.x, p1.y, 3, 'red')
    square(p2.x, p2.y, 3, 'blue')
    update()
    ontimer(draw(), 50)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1Aim.rotate(90), 'a')
onkey(lambda: p1Aim.rotate(-90), 'd')
onkey(lambda: p2Aim.rotate(90), 'j')
onkey(lambda: p2Aim.rotate(-90), 'l')
draw()
done()
