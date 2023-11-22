from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Create and manage scoreboard of the game."""
    def __init__(self):
        """Initialize scoreboard on the screen."""
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.goto(x=-200, y=250)
        self.print_score()

    def print_score(self):
        """Write score / level on screen."""
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        """Update score of the player when it crosses finish line."""
        self.level += 1
        self.print_score()

    def game_over(self):
        """Print GAME OVER in the center of the scree."""
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align="center", font=FONT)
