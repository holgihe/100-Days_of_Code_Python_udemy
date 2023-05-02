#!/usr/bin/env python3
####################################################################
#           - Day025_US-States-Games.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - CSV-Data exercise with PANDAS python-module.
#           - Game to remember the names of US-States
#           -
#           - https://www.sporcle.com/games/g/states?t=unitedstates
#
# Input:    - Day025_US-States-Game_50states.csv
#           - Day025_US-States-Game_blankstates_img.gif
#
# Todo:     - TODO  - Finish code:  game counter, game_is_on variable, Highscore, ...
#           - TODO  - change to OOP code with Classes !!
#           - TODO  - Pandas module - learn & practice
#           - TODO  - Simplify code according to Day026-Video238 (List comprehension)
#           -   -
#
# Version   (1.0) 2023-04-30    New created
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
INPUT_DATA_FILE = "Day025_US-States-Game_50states.csv"
INPUT_BACKGROUND_IMAGE_MAP = "Day025_US-States-Game_blankstates_img.gif"
SCREENWIDTH=1400
SCREENHEIGHT=800
MAX_X_COORD=int(SCREENWIDTH/2)
MAX_Y_COORD=int(SCREENHEIGHT/2)



from turtle import Turtle, Screen
import pandas

def get_coordinates(x, y):
     print(x, y)

def write_state_on_screen(x, y, statename):
     state = Turtle()
     state.penup()
     state.hideturtle()
     state.setpos(x, y)
     state.write(statename)

with open(INPUT_DATA_FILE) as csvfile:
     us50states = pandas.read_csv(csvfile)
     print(type(us50states))
     print(us50states.dtypes)
     print(us50states)
     all_states_list = us50states.state.to_list()
     print(all_states_list)

screen = Screen()
backgrnd = Turtle()
screen.setup(width=SCREENWIDTH, height=SCREENHEIGHT)
screen.bgcolor("white")
screen.title("US-States Quiz - Name the 50 states !!")
#screwrien.tracer(0)
screen.update()
screen.register_shape(INPUT_BACKGROUND_IMAGE_MAP)
backgrnd.shape(INPUT_BACKGROUND_IMAGE_MAP)
#screen.update()
screen.onclick(get_coordinates)

while 1:
   user_answer = screen.textinput(title="Guess a state", prompt="What's another state's name ?")
   if user_answer in all_states_list:
        state_guessed = us50states[us50states.state==user_answer]
        print(state_guessed.state.item())
        write_state_on_screen(int(state_guessed.x), int(state_guessed.y), state_guessed.state.item())



       # for state in us50states:
#      print(type(state))
#     # print(state["x"], state["y"], state["state"])
#      write_state_on_screen(-297, 13, "California")
screen.mainloop()


#screen.exitonclick()
