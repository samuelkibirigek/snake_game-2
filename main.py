from turtle import Screen
from snake import Snake

screen = Screen()
snake = Snake()

screen.setup(width=600, height=600)
screen.bgcolor("black")

game_is_on = True
while game_is_on:
    snake.move()


screen.exitonclick()

