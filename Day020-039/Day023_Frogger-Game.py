#!/usr/bin/env python3
####################################################################
#           - Day022_Frogger-Game_oop.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Classic Frogger Game from ATARI.
#           -
#
# Input:    -
#           -
# Output:   -
#           -
#
# Todo:     -  ok - Create Screen
#           -  ok - Create and move frog (only up, left, right)
#           -  ok - Create cars & move them
#           -  ok - Detect collision frog with any car
#           -  ok - Detect when frog reaches other side of the street (top of screen)
#           -  ok - Calculate Scoreboard
#           -  - Improve distribution of cars on screen, especially on start
#           -  - Create level, so with each successfull run, it gets faster, with more cars
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
from random import randint, choice


# Constants & Variables
#
SCREENWIDTH=800
SCREENHEIGHT=600
MAX_X_COORD=int(SCREENWIDTH/2)
MAX_Y_COORD=int(SCREENHEIGHT/2)

game_is_on=True
max_cnt_cars=20
car_list = []

# Classes
#
class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setpos(0, -MAX_Y_COORD+30)
        self.shapesize(1.5, 1.5)
        self.setheading(90)

    def up(self):
        if self.ycor() < MAX_Y_COORD:
           self.sety(self.ycor()+10)
    def left(self):
        if self.xcor() > -MAX_X_COORD:
           self.setx(self.xcor()-10)
    def right(self):
        if self.xcor() < +MAX_X_COORD:
            self.setx(self.xcor()+10)

    def reset(self):
        self.setpos(0, -MAX_Y_COORD+30 )

class Car(Turtle):
    def __init__(self):
        self.car_colours = ["red", "blue", "green", "orange", "grey", "brown"]
        self.car_lines=[ -210, -180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180, 210, 240, 270]
        super().__init__()
        self.shape("square")
        self.color(choice(self.car_colours))
        self.penup()
        self.setheading(180)
        self.shapesize(1,4)
        self.setpos(MAX_X_COORD, choice(self.car_lines))

    def move(self):
        self.setx(self.xcor()-1)

    def disappeared_left(self):
        if self.xcor() < -MAX_X_COORD-40:
            return True

class Scoreboard(Turtle):
  def __init__(self):
     super().__init__()
     self.score = 0
     self.penup()
     self.hideturtle()
     self.color("white")
     self.setpos(0, MAX_Y_COORD-40)
     self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

  def add_score(self):
     self.score += 1
     self.clear()
     self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

  def game_over(self):
     self.setpos(0, 0)
     self.write(f"Game Over !\nFinal Score: {self.score}", align="center", font=("Arial", 28, "normal"))


# Initiate Screen (window)
screen = Screen()
screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
screen.bgcolor("black")
screen.title("Frog Game - Cross the street ! (move with keys 'o', 'k', 'l')")
screen.tracer(0)
screen.update()


frog = Frog()
screen.update()


scoreboard = Scoreboard()

screen.listen()
screen.onkey(frog.up, "o")
screen.onkey(frog.left, "k")
screen.onkey(frog.right, "l")


# Main
while game_is_on:
    time.sleep(0.02)
    screen.update()
    # If Frog reaches upper screen border --> add point on scoreboard, and reset frog to bottom
    if frog.ycor() > MAX_Y_COORD-30:
        scoreboard.add_score()
        frog.reset()
    # Move every car on the screen. If a car reached left screen border, eliminate it.
    # Also check for collision with Frog --> then Game Over !
    for car in car_list:
        car.move()
        if car.disappeared_left():
            car_list.remove(car)
        if car.distance(frog) < 30:
            scoreboard.game_over()
            game_is_on = False

    if len(car_list) < max_cnt_cars and randint(1, 20)==1:
    # add cars as needed, so always are max_cnt_cars on the screen
       car=Car()
       car_list.append(car)
    screen.update()

screen.exitonclick()
