from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Create and control turtle for the game."""
    def __init__(self):
        """Initialize the turtle and place it on the STARTING_POSITION."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """Move the turtle upwards by MOVE_DISTANCE."""
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        """Go to starting position."""
        self.goto(STARTING_POSITION)

    def crossed_finish_line(self):
        """Check whether player has crossed the finish line."""
        return self.ycor() >= FINISH_LINE_Y

