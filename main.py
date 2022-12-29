from turtle import Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)  # turn off the tracer IOT tell the screen when to refresh by using .update() method

snake = Snake()

screen.listen()  # waiting for a keystroke
screen.onkey(key="Left", fun=snake.go_left)  # move to left when left arrow is pressed
screen.onkey(key="Right", fun=snake.go_right)
screen.onkey(key="w", fun=snake.go_up)
screen.onkey(key="s", fun=snake.go_down)

game_on = True
while game_on:
    screen.update()  # refresh the screen after all segments moved forward
    sleep(0.1)
    snake.move()

screen.exitonclick()
