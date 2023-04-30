#!/usr/bin/env python3
####################################################################
#           - Day019_Turtle-Race.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Turtles racing across the screen (using Turtle module).
#           - Bet, which one will win !!
#
# Input:    - Your bet, which turtle will win
#           -
# Output:   -
#           -
#
# Todo:     -
#
# Version   (1.0) 2023-04-16    New created
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


from turtle import Turtle, Screen
from random import randint


WINDOWWIDTH = 1000
WINDOWHEIGHT = 800
QTYTURTLES = 10
COLORS = ["red", "blue", "green", "yellow", "black", "brown", "grey", "orange", "cyan", "magenta"]

turtles = []
race_is_on = False
screen = Screen()
screen.setup(WINDOWWIDTH,WINDOWHEIGHT)

for i in range(0, QTYTURTLES):
  turtles.append(Turtle(shape="turtle"))
  turtles[i].penup()
  turtles[i].color(COLORS[i])
  turtles[i].goto((30-WINDOWWIDTH/2), (40-WINDOWHEIGHT/2+(i*(WINDOWHEIGHT-100)/QTYTURTLES)))

#screen.clear()
user_bet = screen.textinput(title="Make Your bet", prompt="Which Turtle no. will win ?")

if user_bet:
  race_is_on = True

while race_is_on:
   random_distance = randint(5,30)
   random_turtle = randint(0,QTYTURTLES-1)
   turtles[random_turtle].forward(random_distance)
   position = (turtles[random_turtle].position())
   if position[0] >= WINDOWWIDTH/2:
     race_is_on = False
     print(f"Turtle nr. {random_turtle+1} won !!")
     if random_turtle+1 == user_bet:
       print(f"Your turtle nr. {user_bet} won. Very Good !!")
     else:
       print(f"Another turtle nr. won. You lost !!")


screen.exitonclick()
