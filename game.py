import time
# from turtle import Turtle
from turtle import Screen, Turtle

from snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()

food = Turtle("circle")
food.shapesize(0.5, 0.5)
food.color("red")
# food.goto(0, 0)

screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")


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
    time.sleep(0.5)

    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)

    # segments[0].forward(20)
    # segments[0].left(90)

    snake.move()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        # snake.reset()

screen.exitonclick()
