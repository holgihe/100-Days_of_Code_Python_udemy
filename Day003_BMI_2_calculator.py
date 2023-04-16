#!/usr/bin/env python3
####################################################################
#           - Day003_BMI_2_calculator.py --
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Calculates Your body's BMI Body-Mass-Index
#           ...
# Input:    - Height (m)
#           - Weight (kg)
# Output:   - BMI with indication classification
#           ..
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
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / ((height ** 2))
print (f"{weight} / ({height} x {height}) = {bmi}")

if bmi <= 18.5:
    print (f"Your BMI is {int(round(bmi,0))}, You are underweight.")
elif bmi <= 25:
    print (f"Your BMI is {int(round(bmi,0))}, You have normal weight.")
elif bmi <=30:
    print (f"Your BMI is {int(round(bmi,0))}, You are slightly overweight.")
elif bmi <=35:
    print (f"Your BMI is {int(round(bmi,0))}, You are obese.")
else:
    print (f"Your BMI is {int(round(bmi,0))}, You are clinically obese.")
