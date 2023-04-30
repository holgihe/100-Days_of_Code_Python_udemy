#!/usr/bin/env python3
####################################################################
#           - Day024_Mass-Mail-Merger.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Serial Letter/Mail program.
#           -
#
# Input:    - EMail form, with common text + data fields
#                              (./Day024_Mass-Mail-Merger/Input/Letters/starting_letter.txt)
#           - File with data to fill out data fields
#                              (./Day024_Mass-Mail-Merger/Input/Names/invited_names.txt)
# Output:   - txt-files with mail content, one for each entry in data file
#                              (./Day024_Mass-Mail-Merger/Output/ReadyToSend/xxx.txt)
#
# TODO:         Create a letter using starting_letter.txt
#                    for each name in invited_names.txt
#                    Replace the [name] placeholder with the actual name.
#                    Save the letters in the folder "ReadyToSend".
#
#                    Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#                    Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#                    Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# Todo:     - ok  - Create function to read file with names, store in list
#           - ok  - All the rest !
#
# Version   (1.0) 2023-04-24    New created
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

# Constants & Global Variables

INPUT_NAMES_DIR = "./Day024_Mass-Mail-Merger/Input/Names/"
INPUT_NAMES_FILE = "invited_names.txt"
INPUT_LETTER_DIR = "./Day024_Mass-Mail-Merger/Input/Letters/"
INPUT_LETTER_FILE = "starting_letter.txt"
OUTPUT_LETTER_DIR = "./Day024_Mass-Mail-Merger/Output/ReadyToSend/"


# Open file with names, and store in list of strings
names_file = open(INPUT_NAMES_DIR+INPUT_NAMES_FILE, "r")
names = names_file.readlines()
names_mod = []

for name in names:
    # Remove newlines from strings
    names_mod.append(name.replace("\n", ""))
    print(names_mod)

# Open file with Letter, and store in list of strings
#
letter_file = open(INPUT_LETTER_DIR+INPUT_LETTER_FILE, "r")
letter_lines_org = letter_file.readlines()
letter_lines_mod = []

for name in names_mod:
   file_write = open(OUTPUT_LETTER_DIR+name+".txt", "x")
   for line in letter_lines_org:
       # Replace [name] field with name from database, and write to according txt file
       file_write.write(line.replace("[name]", name))

