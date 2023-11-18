#!/usr/bin/env python3
####################################################################
#           - Day024_Mass-Mail-Merger.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Mass Mail system.
#           -
#
# Input:    - Standard Letter (with data fields)
#           - Data File (names of recipients)
# Output:   - Mail messages (as text files)
#           -
#
# Todo:     -.
#
# Version
#           (1.0) 2023-04-23    New created
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


from pickle import FALSE
from turtle import Screen, Turtle
import time
from random import randint

# Constants & Variables
#
SCREENWIDTH=800
SCREENHEIGHT=600
MAX_X_COORD=int(SCREENWIDTH/2)
MAX_Y_COORD=int(SCREENHEIGHT/2)
STARTING_POSITIONS=[(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0), (-160, 0), (-180, 0), (-200, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

game_is_on = True

# Classes
#
class Snake:
  def __init__(self, starting_positions):
    self.starting_positions=starting_positions
    self.segments = []
    self.heading=0
    self.create_snake()

  def create_snake(self):
    for position in self.starting_positions:
       new_segment=Turtle(shape="square")
       new_segment.color("white")
       new_segment.penup()
       new_segment.setpos(position)
       self.segments.append(new_segment)

  def move(self):
    for seg_num in range(len(self.segments)-1, 0, -1):
        #If not first [0] Segment, then move from last to first to the position of the antecessor
        self.segments[seg_num].setpos(self.segments[seg_num-1].pos())
    self.segments[0].forward(MOVE_DISTANCE)
    screen.update()
    time.sleep(0.15)

  def extent(self):
    # With each food eaten, snake gets longer by one element
    new_segment=Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_pos=self.segments[-1].pos()
    new_segment.setpos(new_pos)
    self.segments.append(new_segment)

  def reset(self):
    for segment in self.segments:
      segment.setpos(MAX_X_COORD+100, MAX_Y_COORD+100)
    self.segments.clear()
    self.create_snake()

  def up(self):
    if self.segments[0].heading() != DOWN:
      self.segments[0].setheading(UP)

  def down(self):
    if self.segments[0].heading() != UP:
      self.segments[0].setheading(DOWN)

  def left(self):
    if self.segments[0].heading() != RIGHT:
      self.segments[0].setheading(LEFT)

  def right(self):
    if self.segments[0].heading() != LEFT:
      self.segments[0].setheading(RIGHT)

class Food(Turtle):
  def __init__(self):
     super().__init__()
     self.penup()
     self.color("blue")
     self.shape("circle")
     self.refreshpos()
     self.shapesize(0.5, 0.5)

  def refreshpos(self):
       x_coord=20*randint(int(-(MAX_X_COORD-20)/20), int(+(MAX_X_COORD-20)/20))
       y_coord=20*randint(int(-(MAX_Y_COORD-20)/20), int(+(MAX_Y_COORD-20)/20))
       self.setpos(x_coord, y_coord)

class Scoreboard(Turtle):
  def __init__(self):
     super().__init__()
     self.score = 0
     self.highscore = 0
     with open("Day020_Snake-Game_highscore.txt") as highscore_datafile:
       self.highscore = int(highscore_datafile.read())
     self.penup()
     self.hideturtle()
     self.color("white")
     self.setpos(0, MAX_Y_COORD-40)
     self.update_scoreboard()

  def update_scoreboard(self):
     self.clear()
     self.write(f"Score: {self.score}    -   HighScore: {self.highscore}", align="center", font=("Arial", 20, "normal"))


  def add_score(self):
     self.score += 1
     self.clear()
     self.update_scoreboard()
#     self.write(f"Score: {self.score}\nHigh Score: {self.highscore}", align="center", font=("Arial", 20, "normal"))

  def reset(self):
     if self.score > self.highscore:
       self.highscore = self.score
       with open("Day020_Snake-Game_highscore.txt", mode="w") as highscore_datafile:
         highscore_datafile.write(f"{self.highscore}")
     self.score = 0
     self.update_scoreboard()

  def game_over(self):
     #self.setpos(0, 0)
     self.write(f"Game Over !\nYour Score: {self.score}", align="center", font=("Arial", 28, "normal"))


# Initiate Screen (window)
screen = Screen()
screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
screen.bgcolor("black")
screen.title("Snake Game - Have fun !")
screen.tracer(0)
screen.update()
# Cre0te snake object
snake = Snake(STARTING_POSITIONS)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
scoreboard = Scoreboard()


# Main
while game_is_on:
  snake.move()
    #time.sleep(0.2)
  screen.update()
  if snake.segments[0].distance(food) < 15:
    # Snake head has eaten the food. Plus one point, and new Food Position !
    print("Collision with Food !")
    food.refreshpos()
    scoreboard.add_score()
    snake.extent()
  if abs(snake.segments[0].xcor()) > MAX_X_COORD or abs(snake.segments[0].ycor()) > MAX_Y_COORD:
    # if Snake head hits the window limits, the game is over
    game_is_on = False
    scoreboard.game_over()
    scoreboard.reset()
    screen.update()
    game_is_on = True
    snake.reset()

  for segment in snake.segments[1:]:
    if snake.segments[0].distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()
      scoreboard.reset()
      screen.update()
      game_is_on = True
      snake.reset()
      screen.update()




screen.exitonclick()
