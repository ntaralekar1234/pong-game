from turtle import Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong Game")

paddle = Paddle()
screen.exitonclick()