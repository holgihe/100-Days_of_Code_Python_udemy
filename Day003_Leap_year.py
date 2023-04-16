#!/usr/bin/env python3
####################################################################
#           - Day003_Leap_year.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Calculates if a given year is a leap year,
#           with 29. February
# Input:    - Year
#             ..
# Output:   - Text, if it is a leap year
#             ..
# Todo:       ..
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

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#This is how you work out whether if a particular year is a leap year.
#    on every year that is evenly divisible by 4
#    **except** every year that is evenly divisible by 100
#    **unless** the year is also evenly divisible by 400

div4 = year % 4
div100 = year % 100
div400 = year % 400

#print (f"year = {year}; div4 = {div4}; div100 = {div100}; div400 = {div400};")

if (year % 4 != 0):
    print ("Not leap year.")
elif (year % 100 == 0):
    if (year % 400 == 0):
        print("Leap year.")
    else:
        print ("Not leap year.")
else:
    print ("Leap Year.")
