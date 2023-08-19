from turtle import Turtle, Screen
import pandas
from scoreboard import Scoreboard

correct_answers = 0


turtle = Turtle()

turtle.penup()
turtle.hideturtle()

screen = Screen()
score = Scoreboard()

screen.title("GUESS THE US STATES GAME")
screen.setup(width=800, height=600)
screen.bgpic("blank_states_img.gif")



df = pandas.read_csv("50_states.csv")

while True:
    response = screen.textinput(f"{correct_answers}/50 States Correct", "What's another state name?")

    if response.title() in df["state"].values:
        correct_answers += 1
        score.increase_score()
        state_x = df[df["state"] == response.title()].x
        state_y = df[df["state"] == response.title()].y
        turtle.goto(int(state_x), int(state_y))
        turtle.write(response.title())
    else:
        score.reset()
        break

screen.exitonclick()