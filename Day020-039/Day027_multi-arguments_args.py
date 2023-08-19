#!/usr/bin/env python3
####################################################################
#           - Day027_multi-arguments_args.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - Excercises functions with multiple variable arguments *args **kwargs
#           -
#           -
#           -
#
# Input:    -
#           -
#
# Todo:     -   -
#           -   -
#           -   -
#
# Version
#           (1.0) 2023-07-14    New created
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

# Imports, headers

# Constants, Variables
#
# Functions
#

# Many positional arguments:
def add (*args):
    sum = 0
    print(args)
    for n in args:
      sum += n
    return sum

# Many keyword arguments:
def calculate(**kwargs):
    sum = 0
    print(kwargs)
    print(type(kwargs))
    for arg in kwargs:
        if arg == "add":
            sum += kwargs["add"]
        elif arg == "multiply":
            sum *= kwargs["multiply"]
        elif arg == "add2":
            sum += kwargs["add2"]
        elif arg == "add3":
            sum += kwargs["add3"]
        elif arg == "multiply2":
            sum *= kwargs["multiply2"]

    return sum
# Classes
#
# Main
#
# First, we play with *args, that means positional arguments without names
result = add(  1, 2, 3 )
print(result)

result = add ( 1, 2, 3, 4, 5, 6, 7, 8, 9 )
print(result)

result = add(0.3, 0.4, 4)
print(result)
#
# Second, now using **kwargs, so we can give name to the arguments, and position does not matter
result = calculate (add=3, multiply=5, add2=7)
print (f"The result from **kwargs arguments is: {result}")
