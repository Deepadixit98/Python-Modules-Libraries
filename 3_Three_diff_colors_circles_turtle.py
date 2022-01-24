import turtle
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

deepa = turtle.Turtle()  # create a turtle named alex
deepa.shape("turtle")    # alex looks like a turtle


deepa.color("green")    # alex has a color
deepa.right(60)         # alex turns 60 degrees right
deepa.left(60)          # alex turns 60 degrees left
deepa.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,3):
    deepa.circle(20*counter)

deepa.right(120)         # alex turns 60 degrees right
deepa.color("blue")    # alex has a color
deepa.right(60)         # alex turns 60 degrees right
deepa.left(60)          # alex turns 60 degrees left
deepa.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,3):
    deepa.circle(20*counter)

deepa.right(120)         # alex turns 60 degrees right
deepa.color("red")    # alex has a color
deepa.right(60)         # alex turns 60 degrees right
deepa.left(60)          # alex turns 60 degrees left
deepa.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,3):
    deepa.circle(20*counter)



#Write the logic to create the given pattern
#Refer the statements given above to draw the pattern                        