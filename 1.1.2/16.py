# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(100)

# move the turtle to another part of the screen
painter.left(180)
painter.up()
painter.forward(100)
painter.down()
# add code here for an arc
painter.circle(100,180)

# move the turtle to another part of the screen
painter.up()
painter.forward(100)
painter.down()

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(200,120,5)

# move the turtle to another part of the screen
painter.up()
painter.left(45)
painter.forward(300)
painter.down()
# add code here to create a polygon of your choice using the circle method
painter.circle(200,360,9)
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
