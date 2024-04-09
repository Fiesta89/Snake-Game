from turtle import Turtle

original_cord = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for segment in range(0, 3):
            body = Turtle(shape='square')
            body.color('white')
            body.penup()
            body.goto(original_cord[segment])
            self.snake_body.append(body)

    def add_body(self):
        body = Turtle(shape='square')
        body.color('white')
        body.penup()
        body.goto(self.snake_body[-1].pos())
        self.snake_body.append(body)

    def move(self):
        for part in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[part].goto(self.snake_body[part - 1].xcor(), self.snake_body[part - 1].ycor())
        self.snake_head.forward(20)

    def wall_collision(self):
        if (self.snake_head.xcor() > 290 or self.snake_head.xcor() < -295
                or self.snake_head.ycor() > 295 or self.snake_head.ycor() < -290):
            return True

    def body_collision(self):
        for part in self.snake_body[1:]:
            if self.snake_head.distance(part) < 10:
                return True

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
