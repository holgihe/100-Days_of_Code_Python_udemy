#!/usr/bin/env python3
####################################################################
#           - Day003_Pizza_order_practice.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Ask three questions for options of pizza.
#           Calculate then total bill prize of the pizza.
#             Small Pizza: $15
#             Medium Pizza: $20
#             Large Pizza: $25
#               Pepperoni for Small Pizza: +$2
#               Pepperoni for Medium or Large Pizza: +$3
#             Extra cheese for any size pizza: + $1
# Input:    - Size of Pizza
#           - Pepperoni ?
#           - Extra Cheese ?
# Output:   - Bill prize
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
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print (f"Your final bill is: ${bill}")
