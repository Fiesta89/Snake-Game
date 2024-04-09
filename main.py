from turtle import Screen
import time
from snake import Snake
from food import Food
from interface import ScoreBoard

score = ScoreBoard()
food = Food()
snake = Snake()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:  
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food) < 15:
        snake.add_body()
        score.update_score()
        food.create_food()
        for part in snake.snake_body:
            while food.distance(part) < 10:
                food.create_food()
    if snake.wall_collision() or snake.body_collision():
        score.game_over()
        game_on = False


screen.exitonclick()
