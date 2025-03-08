import sys
import time
# from turtle import Turtle
from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard, ALIGNMENT, FONT
from snake import Snake

def stop_game():
    global game_is_on
    game_is_on= False
    snake.beyond_screen()
    food.color("black")
    stop = Turtle()
    stop.hideturtle()
    stop.color("white")
    # stop.write("Game OVER.",align="center", font=("Courier", 20, "normal"))
    stop.write("Game OVER!", align=ALIGNMENT, font=FONT)
    screen.update()
    time.sleep(3)
    sys.exit()

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# food = Turtle("circle")
# food.shapesize(0.5, 0.5)
# food.color("red")
# food.goto(0, 0)


screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
screen.onkey(stop_game, "q")


# segment_1 = Turtle(shape="square")
# segment_1.color("white")
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
#
# segment_2.goto(-20, 0)
# segment_3.goto(-30, 0)

# segments = []
#
# starting_position = [(0, 0), (-20, 0 ), (-30, 0)]
# for position in starting_position:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)

    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)

    # segments[0].forward(20)
    # segments[0].left(90)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        snake.reset()
        scoreboard.reset()

    # Detect collision head with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
