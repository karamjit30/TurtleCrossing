from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Class to create and manage cars on the screen."""
    def __init__(self):
        """Setup car manager."""
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create a car at a random location with a random color."""
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        car.goto(x=320, y=random.randint(-240, 240))
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        """Move the car forward by a certain distance."""
        for car in self.cars:
            car.forward(self.move_distance)

    def remove_cars(self):
        """Remove cars from the list which have gone out of visibility."""
        for car in self.cars:
            if car.xcor() < -350:
                self.cars.remove(car)
                car.clear()

    def level_up(self):
        """Increase the speed of cars."""
        for car in self.cars:
            car.clear()
        self.move_distance += MOVE_INCREMENT

    def collision(self, t):
        """Check whether there is collision between player or any car."""
        for car in self.cars:
            if car.distance(t) < 20:
                return True
        return False
