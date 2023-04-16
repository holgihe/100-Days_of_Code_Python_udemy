#!/usr/bin/env python3
####################################################################
#           - Day018_Turtle_RandomWalk.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  RandomWalk (using Turtle module).
##
##
# Input:    -
#           -
# Output:   -
#           -
#
# Todo:     - Needed check, if turtle moves out of screen window ??
#
# Version   (1.0) 2023-04-12    New created
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


import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [ 0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180,
             195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345]

tim.pensize(7)
tim.speed("fastest")

for i in range(0, 2000):
  tim.setheading(random.choice(directions))
  tim.pencolor(random.choice(colours))
  tim.forward(50)
