from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

logo_colors = ["dvd_video_b_blue.gif", "dvd_video_d_blue.gif", "dvd_video_green.gif",
               "dvd_video_l_blue.gif", "dvd_video_orange.gif", "dvd_video_pink.gif", "dvd_video_purple.gif",
               "dvd_video_red.gif", "dvd_video_white.gif", "dvd_video_yellow.gif"]

ball = Ball()

screen.register_shape(ball.dvd_pic)
ball.shape(ball.dvd_pic)

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() < -270 or ball.ycor() > 270:
        ball.vertical_bounce()

    # Detect collision with paddles
    if ball.xcor() > 290 and ball.distance(r_paddle) < 70 or ball.xcor() < -290 and ball.distance(l_paddle) < 70:
        ball.horizontal_bounce()

        screen.register_shape(ball.dvd_pic)
        ball.shape(ball.dvd_pic)

    # Detect R paddle miss
    if ball.xcor() > 380:
        print("Right paddle miss!!!")
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle miss
    if ball.xcor() < -380:
        print("Left paddle miss!!!")
        ball.reset_position()
        scoreboard.r_point()

    ball.move()

screen.exitonclick()
