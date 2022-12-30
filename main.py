from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameOver import GameOver

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
game_over = GameOver()


screen.listen()  # waiting for a keystroke
screen.onkey(key="Left", fun=snake.go_left)  # move to left when left arrow is pressed
screen.onkey(key="Right", fun=snake.go_right)
screen.onkey(key="Up", fun=snake.go_up)
screen.onkey(key="Down", fun=snake.go_down)

game_on = True
while game_on:
    screen.update()  # refresh the screen after all segments moved forward
    sleep(0.1)  # pause after each screen update/refresh
    snake.move()

    # detect collision with food and reset food location
    if snake.head.distance(food) < 15:
        food.reset_location()
        scoreboard.score_count()
        snake.extend()
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        game_over.inform()
        game_on = False


screen.exitonclick()
