import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
t = turtle.Turtle()

# ! Square
def draw_square():
    t.color("black", "yellow")  
    t.begin_fill()              
    for _ in range(4):
        t.forward(50)
        t.left(90)
        t.forward(50)
    t.end_fill()                

# ! Rectangle
def draw_rectangle():
    t.color("blue", "green")
    t.begin_fill()
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(90)
        t.left(90)
    t.end_fill()

# ! Star
def draw_star():
    t.color("red", "orange")
    t.begin_fill()
    for _ in range(5):
        t.forward(130)
        t.left(144)
    t.end_fill()

draw_rectangle()

t.penup()
t.goto(100, 100)
t.pendown()

draw_square()

t.penup()
t.goto(30, 250)
t.pendown()

draw_star()

screen.exitonclick()