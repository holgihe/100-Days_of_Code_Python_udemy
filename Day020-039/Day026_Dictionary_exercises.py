#!/usr/bin/env python3
####################################################################
#           - Day026_Dictionary_exercises.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - Dictionary exercises
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
# Version   (1.0) 2023-05-02    New created
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

# Constants, Variables
#
# Functions
#
# Classes
#
# Main
#
# 1.) Create new Dictionary from original-Dictionary filtered by a if-condition
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random
students_scores = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >=60}
print(passed_students)

# 2.) You are going to use Dictionary Comprehension to create a dictionary
#     called result that takes each word in the given sentence and calculates
#     the number of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:
result = {word:len(word) for word in sentence.split()}
print(result)
