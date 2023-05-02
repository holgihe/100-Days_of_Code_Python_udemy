#!/usr/bin/env python3
####################################################################
#           - Day026_Lists_exercises.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - Lists exercises
#           - Gaddme to remember the names of US-States
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
# Version   (1.0) 2023-05-01    New created
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
# 1.) FOR-LOOP: add +1 to each number in a list
numbers = [ 2, 5, 7, 14, 129 ]
numbers_new = []
print(numbers)

# 1.1.) Classic for-loop (with better comprehension)
for number in numbers:
     new_num = number+1
     numbers_new.append(new_num)

print(numbers_new)
numbers = numbers + numbers_new
print(numbers)

# 1.2.) Optimized for-loop -->   new_list =  [n+1 for n in old_list]
numbers = [ 2, 5, 7, 14, 129 ]
numbers_new2 = [n+1 for n in numbers]
print(f"Original List:  {numbers}")
print(numbers_new2)
numbers += numbers_new2
print(f"Complete merged list: {numbers}")

# 1.3.) For loop on a string (instead of a list) --> string_new will be a list !!
print("1.3.) For loop on a string (instead of a list)")
string = "Alfonso"
string_new = [n for n in string]
print(string)
print(string_new)

# 2.) For loop using rang() to create a list of doubled integers
print("===========================")
print("list of doubled int using for loop & range()")
list_doubled = []
for n in range(1,5):
     list_doubled.append(2*n)
print(list_doubled)
# 2.1) Now optimized code
print("===========================")
print("Now optimized code:")
list_doubled = []
list_doubled = [2*n for n in range(1,5)]
print(list_doubled)

# 3.) for loop with a condition
print("for loop with a condition inside to extract only some items from a list !!")
list = [1, 4, 5, 7, 9, 12, 15, 16, 18, 19, 20, 21, 34]
print(list)
list_filtered = [n for n in list if (n<18 and n>7)]
print("list_filtered contains then only 7<numbers<18")
print(list_filtered)

# 3.1) for loop with condition - strings
list=[ "Angela", "Heribert", "Anne", "Joe", "Wilkenstein", "Tom", "Jimi", "Jeffrey" ]
print(list)
list_filtered = [name.upper() for name in list if len(name)>4]
# ...and just for fun, convert to upper letters !!
print("list_filtered, only with names with length>4 chars")
print(list_filtered)


# 4.) for loop, calculate square of each number, and store in new list
numbers = [ 1, 4, 5, 7, 9, 12, 15, 20 ]
numbers_squares = [ n*n for n in numbers ]
print(numbers)
print(numbers_squares)


# 5.) Extract from a list only even numbers, and store in new list "result"
print("\n\nExtract from a list only even numbers")
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n%2 == 0]
print(numbers)
print(result)

# 6.) Import two csv-files with numbers, and compare overlap (which numbers are in both lists)
#
# 6.1.) Pandas Dataframes solution:
import pandas

file1 = pandas.read_csv("Day026_Lists_exercises_file1.txt", header=None)
file2 = pandas.read_csv("Day026_Lists_exercises_file2.txt", header=None)
result = []

print("6.) Import two csv-files with numbers, and compare overlap")
print("6.1) My Pandas Dataframe solution:")
for num1 in file1[0]:
    if num1 in file2[0].unique():
        result.append(num1)
# Write your code above 👆
print(result)



# 6.2) Simple List solution (by Angela)
print("6.2) Simple List solution (by Angela):")
with open("Day026_Lists_exercises_file1.txt") as file1:
    list1 = file1.readlines()
with open("Day026_Lists_exercises_file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]
# Write your code above 👆
print(result)
