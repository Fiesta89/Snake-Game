from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('pink')
        self.speed('fastest')
        self.create_food()

    def create_food(self):
        food_cord = (randint(-280, 280), randint(-280, 280))
        self.goto(food_cord)

