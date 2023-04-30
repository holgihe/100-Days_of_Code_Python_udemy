#!/usr/bin/env python3
####################################################################
#           - Day005_Adding_even_numbers.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Sums all even number in the range from 1 to 100
##             .
# Input:    - none
#           -
# Output:   - sum
#           -
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

#Write your code below this row 👇
sum = 0

for number in range(2,101,2):
#    print(number)
    sum += number

print(f"{sum}")
