#!/usr/bin/env python3
####################################################################
#           - Day003_Love_calculator.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.com>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Asks for the names of a couple.
#           Check, how many time the letters of both names are found in
#           the words "TRUE" (=digit1), & "LOVE" (=digit2).
#           Then forms a 2-digit-numer:   digit1;digit2
#           Values > 50 show TRUE LOVE !!!
# Input:    Name1
#           Name2
# Output:   Number
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

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

digit1=0
digit1 += name1_lower.count("t") + name2_lower.count("t")
digit1 += name1_lower.count("r") + name2_lower.count("r")
digit1 += name1_lower.count("u") + name2_lower.count("u")
digit1 += name1_lower.count("e") + name2_lower.count("e")

digit2=0
digit2 += name1_lower.count("l") + name2_lower.count("l")
digit2 += name1_lower.count("o") + name2_lower.count("o")
digit2 += name1_lower.count("v") + name2_lower.count("v")
digit2 += name1_lower.count("e") + name2_lower.count("e")

score = int(digit1)*10 + int(digit2)

if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score <=50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}.")
