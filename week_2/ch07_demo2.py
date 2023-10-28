# Topic : turtle , random Modules
# DEMO

import turtle as turtle
import random as random

# let's check turtle's documentation
# turtle.home()
# turtle.forward(100)  # number of pixels
# turtle.left(120)
# turtle.forward(100)
# turtle.color("green")
# turtle.left(120)
# turtle.forward(100)
#
# turtle.done()

turtle.shape("turtle")
def drawCircle(x, y):
    # Draw a circle there , and fill it with a random color .
    # turtle.up()
    turtle.fillcolor(random.random(), random.random(), random.random()) # Red Green Blue
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    # turtle.up()

turtle.title ("Click on the canvas !")

# bind left mouse button to drawCircle function
turtle.onscreenclick(drawCircle)

# Initiate main loop
turtle.mainloop()


# spaceship game
# http://www.codeskulptor.org/#user43_7zb1ohzfMl_35.py
