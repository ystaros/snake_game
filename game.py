import sys
import time
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

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
screen.onkey(stop_game, "q")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)

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
