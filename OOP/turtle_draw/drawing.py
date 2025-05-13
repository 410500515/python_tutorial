import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(1)

turtle.color('red')
turtle.pensize(5)
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

for _ in range(5):
    turtle.forward(100)
    turtle.right(72)

screen.mainloop()