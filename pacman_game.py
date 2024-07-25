import turtle
import random

turtle.speed(10) 
screen = turtle.Screen()
turtle.speed(10)
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width = 600,height = 600)
screen.title("MK GAME ")

pacman = turtle.Turtle()
pacman.shape("circle")
pacman.speed(8)
pacman.penup()
pacman.color("yellow")
pacman.direction = "stop"

foods = []
for _ in range(150):
    food = turtle.Turtle()
    food.speed(5)
    food.penup()
    food.color("orange")
    food.shape("circle")
    food.shapesize(stretch_wid = 0.4,stretch_len = 0.4)
    x = random.randint(-450,450)
    y = random.randint(-450,450)
    food.setposition(x,y)
    foods.append(food)

def move():
    if pacman.direction =="left":
        x = pacman.xcor()
        x-= 5
        pacman.setx(x)

    if pacman.direction =="right":
        x = pacman.xcor()
        x+= 5
        pacman.setx(x)

    if pacman.direction =="up":
        y = pacman.ycor()
        y+= 5
        pacman.sety(y)
    
    if pacman.direction =="down":
        y = pacman.ycor()
        y-=5
        pacman.sety(y)

    
def move_Left():
    pacman.direction = "left"

def  move_Right():
    pacman.direction = "right"

def move_Up():
    pacman.direction = "up"
    
def move_Down():
    pacman.direction = "down"


screen.listen()
screen.onkey(move_Right,"Right")
screen.onkey(move_Left,"Left")
screen.onkey(move_Up,"Up")
screen.onkey(move_Down,"Down")

while True:
    screen.update()
    for i in foods:
        if pacman.distance(i) < 10:
            x = random.randint(-280,280)
            y = random.randint(-280,280)
            i.goto(x,y)

    move()