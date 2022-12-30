from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

BOARD_COLOR = "black"
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(BOARD_COLOR)
screen.title("Python Snake Game")
screen.tracer(0)  # turn off the tracer IOT tell the screen when to refresh by using .update() method

# initializing snake, food and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # waiting for a keystroke
screen.onkey(key="Left", fun=snake.go_left)  # move to left when left arrow is pressed
screen.onkey(key="Right", fun=snake.go_right)
screen.onkey(key="w", fun=snake.go_up)
screen.onkey(key="s", fun=snake.go_down)

game_on = True
while game_on:
    screen.update()  # refresh the screen after all segments moved forward
    sleep(0.1)  # pause after each screen update/refresh
    snake.move()

    # detect collision with food and reset food location
    if snake.head.distance(food) < 15:
        food.reset_location()
        scoreboard.score_count()

screen.exitonclick()
