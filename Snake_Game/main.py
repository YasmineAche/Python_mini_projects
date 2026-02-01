from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

TOP_BORDER = 270
BOTTOM_BORDER= -270
LEFT_BORDER = -270
RIGHT_BORDER = 270

def start_game():
    global is_game_running
    is_game_running = True
    while is_game_running:
        screen.update()
        time.sleep(0.2)
        my_snake.move()

        if my_snake.snake_head.distance(my_food) < 20:
            my_score.increase_score()
            my_snake.extend_body()
            my_food.move_food()

        if (my_snake.snake_head.xcor() > RIGHT_BORDER
                or my_snake.snake_head.ycor() > TOP_BORDER
                or my_snake.snake_head.xcor() < LEFT_BORDER
                or my_snake.snake_head.ycor() < BOTTOM_BORDER
        ):
            is_game_running = False
            my_score.game_over()

        for snake_body_part in my_snake.snake_body_parts_list[1:]:
            if my_snake.snake_head.distance(snake_body_part) < 10:
                is_game_running = False
                my_score.game_over()


def restart_game():
    my_snake.reset_snake()
    start_game()

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

is_game_running = False

my_snake = Snake()
my_food = Food()
my_score = Scoreboard()

screen.listen()
screen.onkey(fun=my_snake.turn_up, key="Up")
screen.onkey(fun=my_snake.turn_down, key="Down")
screen.onkey(fun=my_snake.turn_right, key="Right")
screen.onkey(fun=my_snake.turn_left, key="Left")
screen.onkey(fun=start_game, key="space")
screen.onkey(fun=restart_game, key="r")

screen.exitonclick()