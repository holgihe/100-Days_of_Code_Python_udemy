#!/usr/bin/env python3
####################################################################
#           - Day012_Guess_the_Number.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Computer thinks a number between 1 and 100.
##             You have to guess the number
##
# Input:    - easy / hard  Level
#           - Number guessed
# Output:   - Too high / Too low / You loose / You Win
#           -
#
# Todo:
#
# Version   (1.0) 2023-03-27    New created
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


#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint

# Import os module for clear() Screen function
import os

def clear():
    # Check if Operating System is Mac and Linux or Windows
   print(os.name)
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

logo = """_______         _______ _______ _______       _               _______ ______  _______ _______
(  ____ |\     /(  ____ (  ____ (  ____ \     ( (    /|\     /(       (  ___ \(  ____ (  ____ )
| (    \| )   ( | (    \| (    \| (    \/     |  \  ( | )   ( | () () | (   ) | (    \| (    )|
| |     | |   | | (__   | (_____| (_____ _____|   \ | | |   | | || || | (__/ /| (__   | (____)|
| | ____| |   | |  __)  (_____  (_____  (_____| (\ \) | |   | | |(_)| |  __ ( |  __)  |     __)
| | \_  | |   | | (           ) |     ) |     | | \   | |   | | |   | | (  \ \| (     | (\ (
| (___) | (___) | (____//\____) /\____) |     | )  \  | (___) | )   ( | )___) | (____/| ) \ \__
(_______(_______(_______\_______\_______)     |/    )_(_______|/     \|/ \___/(_______|/   \__/
"""

TURNS_LEVEL_EASY = 10
TURNS_LEVEL_HARD = 5

def set_difficulty():
  level = input("Choose difficulty ('easy' or 'hard'): ")
  if level == "easy":
    return TURNS_LEVEL_EASY
  else:
    return TURNS_LEVEL_HARD

def game():
  clear()
  print(logo)
  print("Welcome to our number guess games.")
  print("I'm thinking of a number between 1 and 100")
  number_to_guess = randint(1,100)
  print(f"Psst. The number to guess is: {number_to_guess}.")
  nr_guess_left = set_difficulty()
  print(f"Guesses left: {nr_guess_left}.")

  while nr_guess_left > 0:
    number_guessed = int(input("Guess a number:  "))
    if number_guessed == number_to_guess:
      print("You Win !")
      return 0
    elif number_guessed > number_to_guess:
      print("Too high !")
      nr_guess_left -= 1
      print(f"You have {nr_guess_left} guesses left.")
    elif number_guessed < number_to_guess:
      print("Too low !")
      nr_guess_left -= 1
      print(f"You have {nr_guess_left} guesses left.")

  print(f"You loose ! The number was {number_to_guess}.")


game()
