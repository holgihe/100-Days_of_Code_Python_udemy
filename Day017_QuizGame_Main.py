#!/usr/bin/env python3
####################################################################
#           - Day017_QuizGame_Main.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.com>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Quiz Game with Object-Oriented-Programming.
#             - Main.py  file
##
# Input:    -
#           -
# Output:   -
#           -
#
# Todo:
#
# Version   (1.0) 2023-04-10    New created
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


from Day017_QuizGame_question_model import Question
from Day017_QuizGame_data import question_data
from Day017_QuizGame_quizbrain import QuizBrain

question_bank = []

for item in question_data:
  text = item["text"]
  answer = item["answer"]
  new_item = Question(text, answer)
  question_bank.append(new_item)

quizbrain = QuizBrain(question_bank)
while quizbrain.still_has_questions():
  if quizbrain.next_question():
     pass
     print(f"Correct ! Your score is {quizbrain.score}/{quizbrain.question_number}.")
  else:
     pass
     print(f"Wrong !! Your score is {quizbrain.score}/{quizbrain.question_number}.")

print(f"Finished ! Your final score is {quizbrain.score}/{quizbrain.question_number}.")
