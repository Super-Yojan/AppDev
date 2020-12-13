import random
import turtle

turt = turtle.Turtle()

#turt.forward(50)
#turt.right(90)


#turt.pensize(15)

def rect():
    for i in range(4):
        turt.forward(100)
        turt.left(90)


#rect()
#turt.forward(10)
#turt.circle(30)

colors = ["red","green","blue"]

for i in range(0,200,4):
    turt.color(colors[random.randint(0,2)])
    turt.circle(i)
    turt.left(10)

wn = turtle.Screen()
wn.mainloop()
