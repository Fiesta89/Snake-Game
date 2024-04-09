from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.point = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f'Score: {self.point}', align='center', font=('Arial', 24, 'normal'))

    def update_score(self):
        self.point += 1
        self.clear()
        self.write(f'Score: {self.point}', align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER', align='center', font=('Arial', 24, 'bold'))





