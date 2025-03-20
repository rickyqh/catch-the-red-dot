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
screen.setup(1000,1000)
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

game_active = True

timer_display=turtle.Turtle()
timer_display.hideturtle()
timer_display.color("black")
timer_display.speed(0)
timer_display.penup()
timer_display.goto(0,220)

timer_value = 600

#initialize score
score =turtle.Turtle()
score.penup()
score.hideturtle()
score.speed(0)
score.goto(0,-220)
score.color("black")
point=0
#uptate score and timer
# def update_timer():
#     timer.clear()
#     timer.write(f"timer:{countdown} seconds",align='center',font=('Ariel',16))

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
screen.onkey(move_up,"w")
screen.onkey(move_down,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")

screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")

def countdown(time_left):
    global game_active
    timer_display.clear()
    if time_left>0:
        timer_display.write(f'time left: {time_left}', align="center", font=("Courier",24,"normal"))
        screen.ontimer(lambda: countdown(time_left - 1),1000)
    else:
        game_active=False
        timer_display.write("Game Over", align="center", font=("Courier",24,"normal"))

#scoring
countdown(60)
while(game_active):
    screen.update()
    turt.color("orange")
    if turt.distance(dot) < 20:
        turt.color("green")
        point+=1
        update_score()
        x=random.randint(-200,200)
        y=random.randint(-200,200)
        dot.goto(x,y)

turt.hideturtle()

    # else:
    #     dot.hideturtle()
    #     turt.hideturtle()
    #     score.clear()
    #     score.goto(0,0)
    #     score.write(f"Game Over😝score:{point}",align='center',font=('Arial',16))
    #     break

input("Enter to stop: ")
