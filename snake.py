from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, pos):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(pos)
        self.snake_segments.append(snake)

    def move(self):
        for seg in range(len(self.snake_segments)-1, 0, -1):
            self.snake_segments[seg].goto(self.snake_segments[seg - 1].position())
        self.snake_segments[0].forward(20)

    def extend(self):
        position = self.snake_segments[-1].position()
        self.add_segment(position)

    def go_up(self):
        self.head.setheading(90)

    def go_down(self):
        self.head.setheading(270)

    def go_left(self):
        self.head.setheading(180)

    def go_right(self):
        self.head.setheading(0)
