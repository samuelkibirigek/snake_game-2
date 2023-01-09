from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game practice")
screen.tracer(0)

head = snake.snake_segments[0]

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()
    snake.move()
    if head.distance(food) < 15:
        food.reposition_food()
        score.increment_score()
        snake.extend()
    for seg in snake.snake_segments[1:]:
        if head.distance(seg) < 10:
            game_is_on = False

screen.exitonclick()
