from turtle import Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()