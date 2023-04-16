#!/usr/bin/env python3
####################################################################
#           - Day002_Tip_calculator.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Calculates how much every person should pay of shared bill
#           ...
# Input:    - Qty. persons
#           - Total bill value
#           - Tip % to give
# Output:   - Share to pay for each person
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



#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print ("Welcome to the tip calculator !")
totalbill = float(input ("What was the total bill ? "))
percentage_tip = int(input ("What tip percentage You would like to give ? 10, 12 or 15 ? "))

qty_persons = int(input ("How many people to split the bill ? "))

totalbill_brutto = totalbill * (1+percentage_tip/100)

print(f"Each person should pay {round(totalbill_brutto/qty_persons,2)} $." )
