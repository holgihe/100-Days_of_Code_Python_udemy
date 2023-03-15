#!/usr/bin/env python3
####################################################################
#           - Day005_FizzBuzz_Game.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.com>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Small fun game. Checks every number from 1 to 100:
##             a.) can be divided by 3 --> "Fizz"
##             b.) can be divided by 5 --> "Buzz"
##             c.) can be divided by 3 and also by 5 --> "FizzBuzz"
##             d.) else --> print the number
# Input:    - none
#           -
# Output:   - "Fizz", "Buzz", "FizzBuzz", or the number
#           -
#
# Todo:
#
# Version   (1.0) 2023-02-03    New created
#
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

#Write your code below this row 👇
# A.) My simple own solution:
for number in range(1,101):
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    if number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 != 0 and number % 5 != 0:
        print(f"{number}")

# B.) Better optimized solution:
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
