from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(x=-180, y=270)
        self.hideturtle()
        self.new_score()


    def new_score(self):
        self.write(f"Level: {LEVEL}", align='right', font=FONT)


    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
