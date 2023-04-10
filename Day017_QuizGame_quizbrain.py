#!/usr/bin/env python3
####################################################################
#           - Day017_QuizGame_quizbrain.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.com>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Quiz Game with Object-Oriented-Programming.
#             - quizbrain.py  file
#             - Class to handle gameplay
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


class QuizBrain:
  def __init__(self, quest_list):
    self.question_number = 0
    self.question_list = quest_list
    self.score = 0

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    question = self.question_list[self.question_number]
    self.question_number +=1
    self.answer = input (f"Q.{self.question_number} - True/False:  {question.text} --> ")
    if self.answer == question.answer:
      self.score += 1
      return True
    else:
      return False
