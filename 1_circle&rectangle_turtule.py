import turtle # allows us to use the turtles library

wn = turtle.Screen() # creates a graphics window
wn.setup(400,400) # set window dimension

circle_rad=50 # setthe radius
rectangle_width=150 #set the width
rectangle_height=80 #set the height

Deepa = turtle.Turtle() # create a turtle named deepa
Deepa.shape("turtle") # deepa looks like a turtle
Deepa.color('red') # deepa has a color
Deepa.circle(circle_rad)
Deepa.backward(rectangle_width/2)
Deepa.forward(rectangle_width)
Deepa.right(90)
Deepa.forward(rectangle_height)
Deepa.right(90)
Deepa.forward(rectangle_width)
Deepa.right(90)
Deepa.forward(rectangle_height)