from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def exit_game():
    global is_game_on
    is_game_on = False

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
my_screen.tracer(0)

right_paddle = Paddle(x=350)
left_paddle = Paddle(x=-350)
my_ball = Ball()
my_scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(right_paddle.move_up, "Up")
my_screen.onkey(right_paddle.move_down, "Down")
my_screen.onkey(left_paddle.move_up, "w")
my_screen.onkey(left_paddle.move_down, "s")
my_screen.onkey(exit_game, key="q")

is_game_on = True
while is_game_on:
    time.sleep(my_ball.moving_speed)
    my_screen.update()
    my_ball.move()

    # check if ball collided with a paddle, if so increase its speed
    if my_ball.check_collision(right_paddle,left_paddle):
        my_ball.increase_speed()

    # check if ball went beyond right border
    if my_ball.xcor() > 350:
        my_ball.losing_game()
        my_scoreboard.left_score += 1
        my_scoreboard.write_score()

    # check if ball went beyond left border
    if my_ball.xcor() < -350:
        my_ball.losing_game()
        my_scoreboard.right_score += 1
        my_scoreboard.write_score()

my_screen.bye()