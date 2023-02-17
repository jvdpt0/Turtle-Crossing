from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.level()

    def level(self):
        self.clear()
        self.goto(-220,240)
        self.write('Level:', align='center', font=FONT)
        self.goto(-150,240)
        self.write(self.current_level, align='center', font=FONT)

    def increase_level(self):
        self.current_level +=1
        self.level()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=FONT)