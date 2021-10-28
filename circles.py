import turtle as tu

# Set up parameters
tu.setup(width=800, height=600)
tu.setworldcoordinates(-200,-150,200,150)
tu.speed(10)
#tu.tracer(25)
#tu.ht() # hide turtle
tu.colormode(255)
tu.bgcolor(0,0,0)
tu.pencolor(255,0,0)
tu.pensize(3)

# Draw circles
for i in range(40):
    tu.left(9)
    tu.circle(70)

# Make window closeable
tu.done()
