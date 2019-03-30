from turtle import *
from base import line


def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawX(x, y):
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)



def drawO(x, y):
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawX, drawO]


def tap(x, y):
    "Draw X or O in tapped square."
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
