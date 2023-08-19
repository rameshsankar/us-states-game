from turtle import Turtle
LALIGNMENT = "left"
RALIGNMENT = "right"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scoredata.txt", "r") as f:
            self.high_score = int(f.read())
        self.display_score()

    def display_score(self):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=LALIGNMENT, font=FONT)
        self.write(f"High Score: {self.high_score}    ", align=RALIGNMENT, font=FONT)

    def reset(self):
        self.goto(0, 0)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scoredata.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 10
        self.update_score()
