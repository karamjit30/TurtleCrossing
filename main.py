import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create and setup window for the game
window = Screen()
window.setup(width=600, height=600)
window.title("Turtle Crossing")
window.tracer(0)

# Create turtle for the game
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for keypress event
window.listen()
window.onkey(fun=player.move_up, key="Up")

# Game loop
car_count = 0  # A variable to limit the number of cars on screen
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if car_count % 6 == 0:  # Create car after every 6th time loop runs
        car_manager.create_car()
    car_manager.move_cars()
    car_manager.remove_cars()
    car_count += 1
    window.update()
    # Below statement only for debugging
    # print(len(car_manager.cars))

    # Check whether player has crossed finished line
    if player.crossed_finish_line():
        player.refresh()
        car_manager.level_up()
        scoreboard.update_score()

    # Check collision between player and car(s)
    if car_manager.collision(player):
        game_is_on = False
        scoreboard.game_over()

window.exitonclick()
