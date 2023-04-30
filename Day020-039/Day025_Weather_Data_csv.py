#!/usr/bin/env python3
####################################################################
#           - Day025_Weather_Data_csv.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  csv file-reading exercise.
#           - Reads weather data pairs from csv file and stores in mulit-dimensional list
#
# Input:    - Day025_weather_data.csv
#                              (./Day025_weather_data.csv)
#
#
# Todo:     - ok  -
#           -   -
#
# Version   (1.0) 2023-04-25    New created
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

#####################################################
# First, simple solution with csv library
# lot of work to get data extracted with for-loop and if-condition
# import csv
# # Constants & Global Variables
# INPUT_DATA_FILE = "Day025_weather_data.csv"
# temperature = []

# with open(INPUT_DATA_FILE) as csvfile:
#      print("hello")
#      weather_data = csv.reader(csvfile)
#      for row in weather_data:
#           print(row)
#           if row[1] != "temp":
#                temperature.append(int(row[1]))
# print(temperature)


####################################################
# Second, with Panda library
#
#
INPUT_DATA_FILE = "Day025_weather_data.csv"
weather_data_string = ""

import pandas
from statistics import mean

with open(INPUT_DATA_FILE) as csvfile:
     weather_data = pandas.read_csv(csvfile)
     print(weather_data.dtypes)
     print(weather_data)
print(weather_data["condition"][0])
print(weather_data["day"][2])
print(type(weather_data))
print(type(weather_data["temp"][0]))

weather_data_string = weather_data.to_string()
print(weather_data_string)

weather_temp_list = weather_data["temp"].to_list()
print(type(weather_temp_list[1]))
print(weather_temp_list)

# print average temperature value
print(f"Average Temperature is: {mean(weather_temp_list)}")
# Now float formatted to 1 decimal only
print(f"Average Temperature is: %.1f" % mean(weather_temp_list))

# print maximum temperature
print(weather_data["temp"].max())
# Alternative calling of temp column data
print(weather_data.temp.max())
print(type(weather_data.temp))

# Search & return rows with specific data content
data_row_monday = weather_data[weather_data.day == "Wednesday"]
print(data_row_monday)
print(type(data_row_monday))

# Find & print row with max temperature
print(weather_data[weather_data.temp == weather_data.temp.max()])
print("\n\n\n")
# Create panda DataFrame from scratch (from a dictionary)
data_dict = {
     "students":  ["Angela", "Tom", "Meike", "Lisa", "Rose"],
     "grades":    ["very good", "average", "poor", "failed", "very good"]}

data_panda = pandas.DataFrame(data_dict)
print(data_panda)

# exxport DataFrame to csv file
data_panda.to_csv("Day025_Weather_Data_csv_export-StudenGrades.csv")
