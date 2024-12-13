"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
#import
import turtle
import random
import time
#initialize screen
screen = turtle.getscreen()
screen.setup(400, 400)
screen.title("This is your screen title")
screen.bgcolor("blue")
#initialize turtle
turt=turtle.getturtle()
turt.shape("turtle")
turt.color("orange")
turt.penup()
#initialize dot
dot=turtle.Turtle()
dot.shape("circle")
dot.color("red")
dot.speed(0)
dot.penup()
#initialize timer
timer=turtle.Turtle()
timer.hideturtle()
timer.color("black")
timer.speed(0)
timer.penup()
timer.goto(0,220)

countdown = 100
#initialize score
score =turtle.Turtle()
score.penup()
score.hideturtle()
score.speed(0)
score.goto(0,-220)
score.color("black")
point=0
#uptate score and timer
def update_timer():
    timer.clear()
    timer.write(f"timer:{countdown} seconds",align='center',font=('Ariel',16))
def update_score():
    score.clear()
    score.write(f"score:{point}",align='center',font=('Arial',16))
#flying dot
x=random.randint(-200,200)
y=random.randint(-200,200)
dot.goto(x,y)
#movement
def move_up():
    turt.setheading(90)
    y=turt.ycor()
    if y < 200:
        turt.sety(y+10)

def move_down():
    turt.setheading(270)
    y=turt.ycor()
    if y > -200:
        turt.sety(y-10)

def move_right():
    turt.setheading(0)
    x=turt.xcor()
    if x < 200:
        turt.setx(x+10)

def move_left():
    turt.setheading(180)
    x=turt.xcor()
    if x > -200:
        turt.setx(x-10)

screen.listen()
screen.onkeypress(move_up,"w")
screen.onkeypress(move_down,"s")
screen.onkeypress(move_left,"a")
screen.onkeypress(move_right,"d")

screen.onkeypress(move_up,"Up")
screen.onkeypress(move_down,"Down")
screen.onkeypress(move_left,"Left")
screen.onkeypress(move_right,"Right")
#scoring
while(True):
    screen.update()
    turt.color("orange")
    if countdown>0:
        countdown-=1
        update_timer()
        if turt.distance(dot) < 20:
            turt.color("green")
            point+=1
            update_score()
            x=random.randint(-200,200)
            y=random.randint(-200,200)
            dot.goto(x,y)

    else:
        dot.hideturtle()
        turt.hideturtle()
        score.clear()
        score.goto(0,0)
        score.write(f"Game Over😝score:{point}",align='center',font=('Arial',16))
        break

input("Enter to stop: ")