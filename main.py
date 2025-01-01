from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

user_paddle = Paddle((350,0))
computer_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(user_paddle.go_up,"Up")
screen.onkey(user_paddle.go_down,"Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    # detect ball contact with user paddle or computer paddle
    if (ball.distance(user_paddle) < 50 and ball.xcor() > 320) or ( ball.distance(computer_paddle) < 50 and ball.xcor() > -320):
        ball.bounce_x()
    # detect ball missed user paddle
    elif ball.xcor() > 380:
        ball.reset_position()

    # detect ball missed computer paddle
    elif ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()