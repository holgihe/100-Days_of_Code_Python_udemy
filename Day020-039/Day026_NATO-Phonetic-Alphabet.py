#!/usr/bin/env python3
####################################################################
#           - Day026_NATO-Phonetic-Alphabet.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - Spells out a word or sentenced
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
NATO_ALPHABET_FILE = "Day026_NATO-Phonetic-Alphabet.csv"
#
# Functions
#
# Classes
import pandas
#
# Main

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
alphabet_data = pandas.read_csv(NATO_ALPHABET_FILE)
#print(alphabet_data)
alphabet = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}
print(alphabet)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word")
print(word)
output_list = [alphabet[letter.upper()] for letter in word]
print(output_list)
