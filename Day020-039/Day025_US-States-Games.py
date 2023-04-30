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
# Todo:     - ok  -
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
INPUT_DATA_FILE = "Day025_Great-Squirrel-Census_Data.csv"
weather_data_string = ""

import pandas
from statistics import mean

with open(INPUT_DATA_FILE) as csvfile:
     census_data = pandas.read_csv(csvfile)
     print(census_data.dtypes)
     print(census_data)

fur_colour_data = census_data["Primary Fur Color"]
print(fur_colour_data)

fur_colour_data_unique = fur_colour_data.unique()
print(fur_colour_data_unique)
print(type(fur_colour_data_unique))
print(fur_colour_data_unique[1])

data_dict = {
         "Fur Colour": [],
         "Count": []
 }

for colour in fur_colour_data_unique:
     count = len(census_data[census_data['Primary Fur Color']==colour])
     print(f"Colour:  {colour}, Count: {count}")
     # Adding value pair to the dictionary
     data_dict["Fur Colour"].append(colour)
     data_dict["Count"].append(count)
     # Alternative way to add key,value pairs - Somehow doesnt work, but why not ?
#     data_dict[colour]=count


print (data_dict)
df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("Day025_Great-Squirrel_Census_Count.csv")

