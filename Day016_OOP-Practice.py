#!/usr/bin/env python3
####################################################################
#           - Day016_OOP_practice.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.com>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Divers testing of Object-Oriented-Programming.
##
##
# Input:    -
#           -
# Output:   -
#           -
#
# Todo:
#
# Version   (1.0) 2023-03-27    New created
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


import turtle
import random

timmy  = turtle.Turtle()
timmy2 = turtle.Turtle()
timmy3 = turtle.Turtle()
timmy4 = turtle.Turtle()
timmy5 = turtle.Turtle()
timmy6 = turtle.Turtle()
timmy7 = turtle.Turtle()
timmy8 = turtle.Turtle()
timmy9 = turtle.Turtle()

timmy.shape("turtle")
timmy5.shape("turtle")
timmy.color("red")

#my_screen = turtle.Screen()
#my_screen.exitonclick()

for _ in range(0, 1000):
   timmy.forward(random.randint(30, 120))
   timmy2.forward(random.randint(30, 120))
   timmy3.forward(random.randint(30, 120))
   timmy4.forward(random.randint(30, 120))
   timmy5.forward(random.randint(30, 120))
   timmy6.forward(random.randint(30, 120))
   timmy7.forward(random.randint(30, 120))
   timmy8.forward(random.randint(30, 120))
   timmy9.forward(random.randint(30, 120))
   timmy.left(random.randint(0, 360))
   timmy2.left(random.randint(0, 360))
   timmy3.left(random.randint(0, 360))
   timmy4.left(random.randint(0, 360))
   timmy5.left(random.randint(0, 360))
   timmy6.left(random.randint(0, 360))
   timmy7.left(random.randint(0, 360))
   timmy8.left(random.randint(0, 360))
   timmy9.left(random.randint(0, 360))



"""
for _ in range(0, 10):
   timmy2.forward(120)
   timmy2.left(90)
   timmy2.forward(120)
   timmy2.left(90)
   timmy2.forward(120)
   timmy2.left(90)
   timmy2.forward(120)
   timmy2.left(90)
   timmy2.left(5)
"""
