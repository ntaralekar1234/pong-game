from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.computer_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.computer_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.user_score, align="center", font=("Courier", 80, "normal"))