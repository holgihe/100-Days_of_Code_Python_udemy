#!/usr/bin/env python3
####################################################################
#           - Day025_Great_Squirrel_Census.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - CSV-Data exercise with PANDAS python-module.
#           - Database is a census of squirrels in New York's central park !
#           -
#           - https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
#           - https://www.thesquirrelcensus.com/
#
# Input:    - Day025_Great-Squirrel-Census_Data.csv
#
# Todo:     - ok  -
#           -   -
#
# Version   (1.0) 2023-04-29    New created
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


# print(weather_data["condition"][0])
# print(weather_data["day"][2])
# print(type(weather_data))
# print(type(weather_data["temp"][0]))

# weather_data_string = weather_data.to_string()
# print(weather_data_string)

# weather_temp_list = weather_data["temp"].to_list()
# print(type(weather_temp_list[1]))
# print(weather_temp_list)

# # print average temperature value
# print(f"Average Temperature is: {mean(weather_temp_list)}")
# # Now float formatted to 1 decimal only
# print(f"Average Temperature is: %.1f" % mean(weather_temp_list))

# # print maximum temperature
# print(weather_data["temp"].max())
# # Alternative calling of temp column data
# print(weather_data.temp.max())
# print(type(weather_data.temp))

# # Search & return rows with specific data content
# data_row_monday = weather_data[weather_data.day == "Wednesday"]
# print(data_row_monday)
# print(type(data_row_monday))

# # Find & print row with max temperature
# print(weather_data[weather_data.temp == weather_data.temp.max()])
# print("\n\n\n")
# # Create panda DataFrame from scratch (from a dictionary)
# data_dict = {
#      "students":  ["Angela", "Tom", "Meike", "Lisa", "Rose"],
#      "grades":    ["very good", "average", "poor", "failed", "very good"]}

# data_panda = pandas.DataFrame(data_dict)
# print(data_panda)

# # exxport DataFrame to csv file
# data_panda.to_csv("Day025_Weather_Data_csv_export-StudenGrades.csv")
