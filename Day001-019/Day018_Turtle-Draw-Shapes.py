#!/usr/bin/env python3
####################################################################
#           - Day018_Turtle-Draw-Shapes.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Draws Polygons (using Turtle module).
##
##
# Input:    -
#           -
# Output:   -
#           -
#
# Todo:
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

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = t.Turtle()
tim.shape("turtle")
tim.pencolor("blue")
########### Challenge 3 - Draw Shapes ########
for edges in range(3, 12):
  angle = 360/edges
  tim.color(random.choice(colours))
  for cnt in range (1, edges+1):
    tim.forward(70)
    tim.right(angle)
