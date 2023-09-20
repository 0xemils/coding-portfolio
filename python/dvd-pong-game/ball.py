from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.dvd_pic = "./img/dvd_video_b_blue.gif"


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def vertical_bounce(self):
        self.y_move *= -1

    def horizontal_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

        self.generate_dvd_color()

    def reset_position(self):
        self.horizontal_bounce()
        self.move_speed = 0.1
        self.goto(0, 0)

    def generate_dvd_color(self):
        logo_colors = ["dvd_video_b_blue.gif", "dvd_video_d_blue.gif", "dvd_video_green.gif", "dvd_video_l_blue.gif",
                       "dvd_video_orange.gif", "dvd_video_pink.gif", "dvd_video_purple.gif",
                       "dvd_video_red.gif", "dvd_video_white.gif", "dvd_video_yellow.gif"]
        self.dvd_pic = f"./img/{random.choice(logo_colors)}"