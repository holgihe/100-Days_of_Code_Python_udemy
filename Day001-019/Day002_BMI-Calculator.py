#!/usr/bin/env python3
####################################################################
#           - Day002_BMI-Calculator.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Caclculates Your BMI - Body-Mass-Index
#           ...
# Input:    - Your body height (m - with . )
#           - Your body weight (kg)
# Output:   - BMI value
# Todo:     ....
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
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight) / (float(height)**2)
#bmi_as_int = int(bmi)
bmi_as_int = round(bmi, 0)

print ("Your BMI is " + str(bmi))
print ("Your BMI is " + str(bmi_as_int))
print (f"Your BMI is {bmi} (used f-Function)")
print (f"Your BMI is {bmi_as_int} (used f-Function)")
