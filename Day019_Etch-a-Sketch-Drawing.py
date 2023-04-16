#!/usr/bin/env python3
####################################################################
#           - Day019_Etch-a-Sketch_Draw.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Simple Drawing program (using Turtle module).
#           -
#
# Input:    - Keyboard Cursor keys to control the Turtle
#           -
# Output:   -
#           -
#
# Todo:     - Needed check, if turtle moves out of screen window ??
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

tim = Turtle()
screen = Screen()

def move_forward():
  tim.forward(40)

def move_backward():
  tim.backward(40)


def turn_left():
  tim.left(15)

def turn_right():
  tim.right(15)

def clear():
  tim.setheading(0)
  tim.goto(0,0)
  tim.clear()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
