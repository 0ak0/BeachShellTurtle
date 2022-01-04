from turtle import Screen, Turtle

topcolor = (0.57254, 0.93333, 0.66275)  # (146, 238, 169)
bottomcolor = (0.39608, 0.64706, 0.45882)  # (101, 165, 117)

screen = Screen()


width, height = screen.window_width(), screen.window_height()

deltas = [(hue - topcolor[index]) / height for index, hue in enumerate(bottomcolor)]

turtle = Turtle()
turtle.color(topcolor)
turtle.speed(0)
turtle.penup()
turtle.goto(-width/2, height/2)
turtle.pendown()

direction = 1

for distance, y in enumerate(range(height//2, -height//2, -1)):

    turtle.forward(width * direction)
    turtle.color([topcolor[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

screen.exitonclick()