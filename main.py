from turtle import Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong Game")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.go_up(),"Up")
screen.onkey(paddle.go_down(),"Down")


screen.exitonclick()