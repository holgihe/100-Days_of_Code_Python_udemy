#!/usr/bin/env python3
####################################################################
#           - Day027_tkinter-exercises.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - tkinter, GUI package for Python
#           -
#           -
#           -
#
# Input:    -
#           -
#
# Todo:     -   -
#           -   -
#           -   -
#
# Version
#           (1.0) 2023-05-12    New created
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

# Imports, headers
import tkinter

# Constants, Variables
#
# Functions
#
def mybuttonclose_clicked():
    print("Buttonclose_clicked")
    mybuttonclose.flash()
    mybuttonclose.flash()
    mybuttonclose.flash()
    mybuttonclose.flash()
    mybuttonclose.flash()
    window.title("Hey You clicked the close Button")
    #exit(0)

def mybutton_clicked():
    print("myButton_clicked")
    mybutton.flash()
    mybutton.flash()
    mybutton.flash()
    mybutton.flash()
    mybutton.flash()
    window.title("Hey You clicked the myButton")
    mylabel["text"]="mybutton clicked !"
    #exit(0)
#

# Classes
#
# Main
#
window = tkinter.Tk()
window.title("tkinter exercises !! Yeah")
window.minsize(width=600,height=400)
#
mylabel = tkinter.Label(text="Labelmein", font=("Arial", 24, "bold"), highlightbackground="blue",highlightcolor="red", takefocus=1)
mylabel.pack(side="left")
mybutton = tkinter.Button(text="Button-My", highlightbackground="blue", highlightcolor="red", activeforeground="green", command=mybutton_clicked)
mybutton.pack(side="right")

# tkinter change options/characteristics later:
mybutton["text"]="ClickMe!"
mybutton["activebackground"]="red"

mybuttonclose = tkinter.Button(text="Close", font=("Courier", 26, "bold"), activebackground="gray", relief="sunken")
mybuttonclose.pack(side="top")
mybuttonclose["takefocus"]=1
mybuttonclose["command"]=mybuttonclose_clicked
mybuttonclose.flash()
window.title("Changed title....")


window.mainloop()
