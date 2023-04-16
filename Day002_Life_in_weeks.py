#!/usr/bin/env python3
####################################################################
#           - Day002_Life_in_weeks.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Tells You how many weeks of life You have left until
#           age of 90 years
# Input:    - Current age (years)
#           -
# Output:   - Weeks left until age 90 years
# Todo:     ..
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
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = (90-int(age)) * 365
weeks = (90-int(age)) * 52
months = (90-int(age)) * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
