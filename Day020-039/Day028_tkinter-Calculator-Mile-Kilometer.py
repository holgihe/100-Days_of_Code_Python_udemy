#!/usr/bin/env python3
####################################################################
#           - Day028_tkinter-Calculator-Mile-Kilometer.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - tkinter, GUI package for Python
#           - Calculator Miles to Kilometers
#           -
#           -
#
# Input:    - Miles
#           -
# Output:   - Kilometers
#
# Todo:     -   -
#           -   -
#           -   -
#
# Version
#           (1.0) 2023-08-20    New created
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

####################################################################
# Imports, headers
import tkinter

####################################################################
# Constants, Variables
#
####################################################################
# Functions
#
def buttoncalc_clicked ():
    print("buttoncalc_clicked")
    print(float(milesentry.get()) * 1.609347)
    kmentry.config(state="normal")
    kmentry.delete(0, tkinter.END)
#   kmentry.insert(tkinter.END, str(float(milesentry.get()) * 1.609347))
    kmentry.insert(tkinter.END, "{:.3f}".format((float(milesentry.get()) * 1.609347)))
    kmentry.config(state="readonly")
#   pro tip convert float into string with fixed decimals:    "{:.4f}".format(num)

####################################################################
# Classes
#
####################################################################
# Main
#
#Creating a new window and configurations
window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=400, height=100)
window.config(padx=30, pady=30)

milesentry = tkinter.Entry()
milesentry.config(width=15)
milesentry.insert(tkinter.END, str(0.0))
milesentry.config(justify="right")
milesentry.grid(column=1, row=0)

labelfix1 = tkinter.Label(text="Miles")
labelfix1.grid(column=2, row=0)


labelfix2 = tkinter.Label(text="is equal to")
labelfix2.grid(column=0, row=1)

kmentry = tkinter.Entry()
kmentry.config(width=15, background="lightgrey", state="readonly")
kmentry.config(justify="right")
kmentry.grid(column=1, row=1)

labelfix3 = tkinter.Label(text="Km")
labelfix3.grid(column=2,row=1)

buttoncalc = tkinter.Button(text="Calculate", command=buttoncalc_clicked)
buttoncalc.grid(column=1, row=2)

window.mainloop()
