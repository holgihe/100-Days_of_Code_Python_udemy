#!/usr/bin/env python3
####################################################################
#           - Day026_PandasDataFrame_exercises.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - Pandas DataFrame exercises
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
#           (1.0) 2023-05-05    New created
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
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Simple iteration - not useful
for (key,value) in student_data_frame.items():
    print(key)
    print(value)

# Using pandas iterrows() function
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    if row.student == "Angela":
        print(f"Angela's score: {row.score}")
