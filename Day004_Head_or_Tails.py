#!/usr/bin/env python3
####################################################################
#           - Day004_Head_or_Tails.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Small Text Computer Game - Toss coins for Heads or Tails
#             use random module from python
# Input:    -
#           -
# Output:   - Answer:  Heads or Tails
#
# Todo:
####################################################################
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.
# If not, see <http://www.gnu.org/licenses/>.
####################################################################

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲

#Write the rest of your code below this line 👇
import random
number = random.randint(0,1)

if number == 1:
    print("Heads")
else:
    print("Tails")
