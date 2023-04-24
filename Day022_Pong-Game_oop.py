#!/usr/bin/env python3
####################################################################
#           - Day022_Pong-Game_oop.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Classic Ping Pong Game from ATARI.
#           -
#
# Input:    -
#           -
# Output:   -
#           -
#
# Todo:     - ok - Create Screen
#           - ok - Create and move a paddle
#           - ok - Create other paddle
#           - ok - Create & move ball
#           - ok Collision detection of ball with wall, and bounce back
#           - ok Collision detection of ball with paddle
#           - ok Detect when paddle misses
#           - ok Calculate Scoreboard
#
# Version   (1.0) 2023-04-20    New created
#
####################################################################
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; wi thout even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.
# If not, see <http://www.gnu.org/licenses/>.
####################################################################


#from pickle import FALSE
from turtle import Screen, Turtle, distance
import time
#from random import randint

# Constants & Variables
#
SCREENWIDTH=800
SCREENHEIGHT=600
MAX_X_COORD=int(SCREENWIDTH/2)
MAX_Y_COORD=int(SCREENHEIGHT/2)

game_is_on=True


# Classes
#
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)

    def up(self):
        if self.ycor() < MAX_Y_COORD:
           self.sety(self.ycor()+10)
    def down(self):
        if self.ycor() > -MAX_Y_COORD:
           self.sety(self.ycor()-10)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1, 1)
        self.delta_y = 10
        self.delta_x = 10
        self.mvcnt = 0

    def move(self):
        # loop count to slow down the Ball, without slowing down paddle movement
        # Normally below in main() loop would put an time.sleep(0.5), but then keystroke response also is delayed ?
        self.mvcnt += 1
        if self.mvcnt < 180:
            return()
        self.mvcnt = 0
        # Collision Detection with upper/lower walls. Ball should bounce back
        if abs(self.ycor()) >= MAX_Y_COORD-10:
            self.delta_y = -1* self.delta_y
        # Collision Detection with left/right walls, or paddle
        #if abs(self.xcor()) >= MAX_X_COORD-10:
        #    self.delta_x = -1* self.delta_x

        self.newx = self.xcor() + self.delta_x
        self.newy = self.ycor() + self.delta_y
        self.setx(self.newx)
        self.sety(self.newy)

    def reset(self):
        self.setx(0)
        self.sety(0)


class Scoreboard(Turtle):
  def __init__(self):
     super().__init__()
     self.score_l = 0
     self.score_r = 0
     self.penup()
     self.hideturtle()
     self.color("white")
     self.setpos(0, MAX_Y_COORD-40)
     self.write(f"Score: {self.score_l} : {self.score_r}", align="center", font=("Arial", 20, "normal"))

  def add_score_l(self):
     self.score_l += 1
     self.clear()
     self.write(f"Score: {self.score_l} : {self.score_r}", align="center", font=("Arial", 20, "normal"))

  def add_score_r(self):
     self.score_r += 1
     self.clear()
     self.write(f"Score: {self.score_l} : {self.score_r}", align="center", font=("Arial", 20, "normal"))




  def game_over(self):
     self.setpos(0, 0)
     self.write(f"Game Over !\nFinal Score: {self.score_l} : {self.score_r}", align="center", font=("Arial", 28, "normal"))


# Initiate Screen (window)
screen = Screen()
screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.update()


paddle_r = Paddle()
paddle_r.goto(MAX_X_COORD-30, 0)
screen.update()

paddle_l = Paddle()
paddle_l.goto(-MAX_X_COORD+30, 0)
screen.update()

scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(paddle_r.up, "o")
screen.onkey(paddle_r.down, "l")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")


# Cre0te snake object
# Main
while game_is_on:
    #time.sleep(0.5)
    ball.move()
    screen.update()

    if (ball.xcor() < MAX_X_COORD-30) and ball.distance(paddle_r.xcor(),paddle_r.ycor())<50:
        #Check for bounce on right paddle
        ball.delta_x = -10
    elif (ball.xcor() > MAX_X_COORD-10):
        # If not bounced on right paddle, check if ball came out of right screen --> point for left player
        scoreboard.add_score_l()
        ball.reset()


    if (ball.xcor() > -MAX_X_COORD+30) and ball.distance(paddle_l.xcor(),paddle_l.ycor())<50:
        #Check for bounce on left paddle
        ball.delta_x = 10
    elif (ball.xcor() < -MAX_X_COORD+10):
        # If not bounced on left paddle, check if ball came out of left screen --> point for right player
        scoreboard.add_score_r()
        ball.reset()

    if scoreboard.score_r >= 10 or scoreboard.score_l >= 10:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
