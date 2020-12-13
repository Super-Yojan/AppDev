#   a113_tower.py

#   Modify this code in VS Code to alternate the colors of the 

#   floors every three floors

import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

painter.pensize(5)

# starting location of the tower

x = -150

y = -150

# height of tower and a counter for each floor
num_floors = 63

floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  if (floor % 21 == 0):
    x+=60
    y=-150

  if (floor % 3 == 0):  
    painter.color("green")
  elif (floor % 3 == 1):
    painter.color("red")
  elif (floor % 3 == 2):
    painter.color("blue")
  y = y + 5 # location of next floor

  floor = floor + 1
  painter.goto(x, y)
  #draw the floor
  painter.pendown()
  painter.forward(50)



wn = trtl.Screen()

wn.mainloop()
