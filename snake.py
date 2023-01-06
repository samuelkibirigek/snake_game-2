from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_STEPS = 20


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(3):
            segment = Turtle("square")
            segment.color("white")
            segment.goto(STARTING_POSITIONS[_])
            self.segments.append(segment)
            self.move()

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.goto(new_x, new_y)

        self.head.forward(SNAKE_STEPS)








