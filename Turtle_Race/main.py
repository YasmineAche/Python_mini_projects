from turtle import Turtle, Screen
from random import randint
"""
Turtle Race Game

This program implements a simple turtle racing game using Python's `turtle` module.
Multiple turtle racers move forward by random distances until one reaches the finish line.

Features:
- Randomized turtle movement
- Visual finish line and winner announcement
- Keyboard controls:
    - Space: start the race
    - R: reset and restart the game
- Clean separation of game logic, race state, and UI elements
"""

def start_race() -> None:
    """
    Starts the turtle race if the game is initialized and no race is currently running.

    This function updates the global race state and triggers the turtle movement.
    It prevents restarting the race while one is already in progress.
    """
    global is_race_on, is_init_game
    if not is_race_on and is_init_game:
        is_race_on = True
        is_init_game = False
        move_turtles()

def move_turtles() -> None:
    """
    Moves all turtles forward by a random distance until one reaches the finish line.

    Each turtle advances randomly on every loop iteration.

    When a turtle crosses the finish line, the race stops and the winner is announced.
    """
    global is_race_on
    while is_race_on:
        for fakroun_racer in fakroun_list:
            random_distance = randint(0, 10)
            fakroun_racer.forward(random_distance)
            fakroun_position = fakroun_racer.xcor()
            if fakroun_position >= 210:
                winner = fakroun_racer
                is_race_on = False
                show_winner(winner)
                break

def show_winner(winner) -> None:
    """
    Displays the race winner on the screen.

    The announcer turtle moves next to the winning turtle, writes the winner message,
    highlights the winner, and enables restarting the race using the 'r' key.

    :param winner: The Turtle object that won the race
    """
    announcer.right(35)
    announcer.goto(winner.xcor() - 230, winner.ycor())
    announcer.color(winner.fillcolor())
    announcer.write(f"Winner {winner.fillcolor().capitalize()} 🏁", font=("Arial", 24, "normal"))
    announcer.color("white")
    announcer.goto(winner.xcor() - 250, winner.ycor())
    winner.circle(20)
    screen.onkey(fun=init_race, key="r")

def init_race() -> None:
    """
    Resets the race to its initial state.

    Clears the winner announcement, repositions all turtles at the starting line, and prepares the game for a new race.
    """
    global is_init_game, y_position
    if is_init_game:
        return
    y_position = 200
    announcer.clear()
    announcer.right(145)
    announcer.goto(0, -230)
    announcer.right(180)
    for fakroun_racer in fakroun_list:
        fakroun_racer.right(180)
        fakroun_racer.goto(-280, y_position)
        y_position -= 70
        fakroun_racer.right(180)
    is_init_game = True

if __name__ == "__main__":
    is_race_on = False
    is_init_game = True
    fakroun_list = []

    screen = Screen()
    screen.setup(width=600, height=500)
    screen.title("Turtle Race")
    screen.bgcolor("black")

    line_drawer = Turtle("turtle")
    announcer = Turtle("turtle")
    line_drawer.color("white")
    announcer.color("white")
    line_drawer.speed(2)
    announcer.speed(2)

    # Position announcer
    announcer.penup()
    announcer.left(90)
    announcer.goto(0, -230)

    # Write key shortcuts
    line_drawer.penup()
    line_drawer.goto(-285, -230)
    line_drawer.pencolor("snow4")
    line_drawer.write("Start race: Space.\nRestart game: r.", font=("Arial", 11, "normal"))

    # Draw finish line
    line_drawer.goto(240, 230)
    line_drawer.pendown()
    line_drawer.pensize(2)
    line_drawer.dot(10)
    line_drawer.right(90)
    line_drawer.forward(430)
    line_drawer.dot(10)
    line_drawer.penup()
    line_drawer.pencolor("white")
    line_drawer.forward(30)
    line_drawer.right(180)

    # Create racers
    y_position = 200
    colors = ["red", "blue", "green", "yellow", "orange", "magenta"]

    for turtle_color in colors:
        fakroun = Turtle(shape="turtle")
        fakroun.penup()
        fakroun.color(turtle_color)
        fakroun.shapesize(2)
        fakroun.goto(-280, y_position)
        y_position -= 70
        fakroun_list.append(fakroun)


    screen.listen()
    screen.onkey(fun=start_race, key="space")
    screen.exitonclick()
