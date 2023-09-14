#!/usr/bin/env python3
####################################################################
#           - Day028_tkinter-widgets-demo.py -
#
# Copyright (C) 2023 holgihe <holgihe@eh-herrgen.com>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - tkinter, GUI package for Python
#           - Demo of different widgets
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
from tkinter import *

####################################################################
# Constants, Variables
#
####################################################################
# Functions
#

#Buttons
def action():
    print("Do something")
#
#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

#Radiobutton
def radio_used():
    print(radio_state.get())

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

####################################################################
# Classes
#
####################################################################
# Main
#
#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=30, pady=30)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
# Test the 3 options to place widget with tkinter:  pack, place, grid
#label.pack()
label.grid(column=0, row=0)


#calls action() when pressed
button = Button(text="Click Me", command=action)
#button.pack()
button.grid(column=4, row=0)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
#entry.pack()
entry.grid(column=0, row=3)
entry.config(relief="groove")

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
#text.pack()
text.grid(column=3, row=3)


#Spinbox
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
#spinbox.pack()
spinbox.grid(column=4, row=4)

#Scale
scale = Scale(from_=0, to=100, command=scale_used)
#scale.pack()
scale.grid(column=3, row=5)

#Checkbutton
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
#checkbutton.pack()
checkbutton.grid(column=0, row=6)

#Radiobutton
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
#radiobutton1.pack()
#radiobutton2.pack()
radiobutton1.grid(column=3, row=6)
radiobutton2.grid(column=3, row=7)


#Listbox
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
#listbox.pack()
listbox.grid(column=3, row=8)

window.mainloop()
