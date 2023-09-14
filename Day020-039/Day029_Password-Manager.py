#!/usr/bin/env python3
####################################################################
#           - Day029_Password-Manager.py -
#
# Copyright (C) 2023 holgihe <holgihe@eh-herrgen.com>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - Simple Password Manager
#           -
#           -
#           -
#
# Input:    -
#           -
# Output:   -
#
# Todo:     -   -
#           -   -
#           -   -
#
# Version
#           (1.0) 2023-08-27    New created
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
import random
from tkinter import messagebox
from tkinter.constants import END

####################################################################
# Constants, Variables
#

###################################################################
# Functions
#
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    if len(website_entry.get()) == 0 or len(user_entry.get()) == 0 or len(passwd_entry.get()) == 0:
        messagebox.showinfo(message = "Some Entries are empty !\nPlease fill all fields.")
    elif messagebox.askokcancel(message = f"Want to add these credentials ?\nWebsite:  {website_entry.get()}\nUser:  {user_entry.get()}\nPassword:  {passwd_entry.get()}"):
        f = open("Day029_Password-M_file.txt", "a")
        f.write(f"{website_entry.get()} | {user_entry.get()} | {passwd_entry.get()}\n")
        f.close()
        website_entry.delete(0, END)
        user_entry.delete(0, END)
        passwd_entry.delete(0, END)
        print("Saved to File")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Here now two versions of the code:  1.)Simple Beginner Code   - 2.)Python-style-Pro code !!
# 1.) Simple Beginner code
#    nr_letters = random.randint(8, 10)
#    nr_symbols = random.randint(2, 4)
#    nr_numbers = random.randint(2, 4)
#    password_list = []
#    for char in range(nr_letters):
#        password_list.append(random.choice(letters))
#    for char in range(nr_symbols):
#            password_list += random.choice(symbols)
#    for char in range(nr_numbers):
#        password_list += random.choice(numbers)
#    random.shuffle(password_list)

    # 2.) Python-Style-Pro Code:
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # Here are two ways to convert the List password_list into a string:
    # 1.) Simple traditional way - for Loop
    #password = ""
    #for char in password_list:
    #  password += char
    #print(f"Your password is: {password}")

    # 2.) Python-Style via  str.Join function - Joins lists or dictionaries or .... into a string.
    #     You can use a separator like this:   " | ".join(password_list)  --> will create string like  "John | Adam | Evangela"
    password = ""
    password = "".join(password_list)
    passwd_entry.delete(0, END)
    passwd_entry.insert(0, password)

####################################################################
# Classes
#
####################################################################
# Main
#

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.minsize(width=550, height=400)
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="Day029_Password-M_Logo.png")
canvas.create_image(100,100, image = logo_image)
canvas.grid(column=1, row=0)

fixtxt_label1 = tkinter.Label(text="Website:", pady=5)
fixtxt_label1.grid(column=0, row=1)
fixtxt_label2 = tkinter.Label(text="EMail/Username:", pady=5)
fixtxt_label2.grid(column=0, row=2)
fixtxt_label3 = tkinter.Label(text="Password:", pady=5)
fixtxt_label3.grid(column=0, row=3)

genpasswd_button = tkinter.Button(text="Create Password", command = generate_password)
genpasswd_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=35, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2, pady=20)


website_entry = tkinter.Entry(width=37)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_entry = tkinter.Entry(width=37)
user_entry.grid(column=1, row=2, columnspan=2)

passwd_entry = tkinter.Entry(width=20)
passwd_entry.grid(column=1, row=3)

window.mainloop()
