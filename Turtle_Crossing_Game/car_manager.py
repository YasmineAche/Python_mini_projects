from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CARS_Y_POSITIONS = [-225, -175, -125, -75, -25, 25, 75, 125, 175, 225]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(0, 6) == 1:
            occupied_lanes = [car.ycor() for car in self.cars_list if car.xcor() > 220]
            available_lanes = [y for y in CARS_Y_POSITIONS if y not in occupied_lanes]

            if available_lanes:
                new_car = Turtle("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.color(choice(COLORS))
                new_car.setheading(180)
                new_car.penup()
                new_car.goto(300, choice(available_lanes))
                self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT