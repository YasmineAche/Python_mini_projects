from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_color_R = 0
        self.snake_color_G = 120
        self.snake_color_B = 0
        self.snake_body_parts_list = []
        self.create_snake_body()
        self.snake_head = self.snake_body_parts_list[0]

    def create_color(self) -> tuple:
        if self.snake_color_R > 180 or self.snake_color_G >= 255:
            self.snake_color_R, self.snake_color_G = 0, 120
        else:
            self.snake_color_R, self.snake_color_G = self.snake_color_R + 20, self.snake_color_G + 15
        return self.snake_color_R, self.snake_color_G

    def create_snake_body(self) -> None:
        for position in START_POSITIONS:
            snake_body_part = self.create_body_part(position)
            self.snake_body_parts_list.append(snake_body_part)

    def create_body_part(self, position) -> Turtle:
        snake_body = Turtle("circle")
        snake_body.shapesize(stretch_wid=1.5, stretch_len=1.5)
        r, g = self.create_color()
        snake_body.color(r, g, self.snake_color_B)
        snake_body.penup()
        snake_body.goto(position)
        return snake_body

    def extend_body(self, score) -> None:
        if len(self.snake_body_parts_list)-3 < score:
            tail_position = self.snake_body_parts_list[-1].position()
            tail = self.create_body_part(tail_position)
            self.snake_body_parts_list.append(tail)
        else:
            self.snake_body_parts_list[score+2].showturtle()

    def move(self) -> None:
        for snake_body_part_index in range(len(self.snake_body_parts_list) - 1, 0, -1):
            next_position = self.snake_body_parts_list[snake_body_part_index - 1].position()
            self.snake_body_parts_list[snake_body_part_index].goto(next_position)
        self.snake_head.forward(MOVING_DISTANCE)

    def turn_left(self) -> None:
        if self.snake_head.heading() == RIGHT:
            return
        self.snake_head.setheading(LEFT)

    def turn_right(self) -> None:
        if self.snake_head.heading() == LEFT:
            return
        self.snake_head.setheading(RIGHT)

    def turn_up(self) -> None:
        if self.snake_head.heading() == DOWN:
            return
        self.snake_head.setheading(UP)

    def turn_down(self) -> None:
        if self.snake_head.heading() == UP:
            return
        self.snake_head.setheading(DOWN)

    def reset_snake(self) -> None:
        i = 0
        [snake_body_part.hideturtle() for snake_body_part in self.snake_body_parts_list]
        for position in START_POSITIONS:
            self.snake_body_parts_list[i].goto(position)
            self.snake_body_parts_list[i].showturtle()
            i += 1
        self.snake_head.setheading(RIGHT)

    def position(self) -> tuple:
        return self.snake_head.position()