import turtle

t = turtle.Turtle('turtle')
s = turtle.Screen()

# DEFINING FEATURES
bw = 100  # base width
bh = 20  # base height
te = 35  # top edge
th = 15  # top height
color = "#761fe0"

s.setup(width=500, height=500, startx=0, starty=0)
t.width(5)
t.speed(0)
t.color(color)


t.fd(bw)  # make the initial base
t.lt(90)
t.fd(bh)
t.penup()
curpos = t.pos()

t.lt(90)  # finish the base sides
t.fd(bw)
t.pendown()
t.rt(90)
t.bk(bh)
t.penup()
t.fd(bh)

t.goto(curpos)  # make the top curvature
t.pendown()
t.rt(90)
t.fd(te)
t.lt(90)
t.fd(th)
t.circle(bw / 2 + te, 180)
t.fd(th)
t.lt(90)
t.fd(te)

t.ht()
print("~~SHELL CREATED~~" +
      "\n Base Width: " +str(bw) +
      "\n Base Height: " + str(bh) +
      "\n Top Edge: " + str(te) +
      "\n Extra Top Height: " + str(th) +
      "\n Color: " + str(color) +
      "\n Series: " + "n/a" +
      "\n~~~~~~~~~~~~~~~~~")
"""
t.goto(0, 0)

message = "test"
t.write(message, font=("Arial", 20, "normal"))
"""

turtle.exitonclick()
