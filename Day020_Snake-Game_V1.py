#!/usr/bin/env python3
####################################################################
#           - Day020_Snake-Game.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Classic Snake Game from first NOKIA cellphones.
#           -
#
# Input:    -
#           -
# Output:   -
#           -
#
# Todo:     -
#
# Version   (1.0) 2023-04-17    New created
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


from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game - Have fun !")
screen.tracer(0)

starting_positions=[(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
  new_segment=Turtle(shape="square")
  new_segment.color("white")
  new_segment.penup()
  new_segment.setpos(position)
  segments.append(new_segment)

screen.update()

game_is_on = True


while game_is_on:
  for seg_num in range(len(segments)-1, -1, -1):
    if seg_num == 0:
      print("First segment")
      segments[seg_num].forward(20)
      segments[seg_num].left(90)
    else:
      #If not first [0] Segment, then move from last to first to the position of the antecessor
      segments[seg_num].setpos(segments[seg_num-1].pos())
     #segments[seg_num].forward(20)
    screen.update()
    time.sleep(0.10)
  #time.sleep(0.2)
  screen.update()



screen.exitonclick()
