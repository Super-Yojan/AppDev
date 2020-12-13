import turtle
import random
import time 
t = turtle.Turtle()

wn = turtle.Screen()
t.speed(0)
t.hideturtle()
wn.screensize(400,400)
def rectangle():
    colors = ["red","green","blue"]
    t.color(colors[random.randint(0,2)])
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()


def draw_rectangles():
    t.up()
    t.setx(random.randrange(0,wn.screensize()[0]))
    t.sety(random.randrange(0,wn.screensize()[1]))
    t.down()
    rectangle()
    time.sleep(1)
    t.clear()


for i in range(50):
    draw_rectangles()





wn.mainloop()
