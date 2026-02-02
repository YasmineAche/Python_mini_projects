import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("gray")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="space")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with a car
    for car in car_manager.cars_list:
        if player.distance(car) < 30:
            is_game_on = False
            scoreboard.write_game_over()

    # detect when player has reached the other side
    if player.is_at_finish_line():
        scoreboard.level += 1
        scoreboard.update_screen()
        player.go_to_starting_position()
        car_manager.increase_speed()

screen.exitonclick()