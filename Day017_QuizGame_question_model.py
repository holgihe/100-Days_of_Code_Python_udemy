#!/usr/bin/env python3
####################################################################
#           - Day017_QuizGame_question_model.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.com>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Quiz Game with Object-Oriented-Programming.
#             - question_model.py  file
#             - Class contains question-answer pairs
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


class Question:
   def __init__(self, q_text, q_answer):
     self.text = q_text
     self.answer = q_answer
