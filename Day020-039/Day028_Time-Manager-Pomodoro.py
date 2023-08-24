#!/usr/bin/env python3
####################################################################
#           - Day028_Time-Manager-Pomodoro.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  - Time Manager based on the book:  The Pomodoro Technique - Francesco Cirillo
#           -
#           -
#           -
#
# Input:    - Buttons:  Start, Reset
#           -
# Output:   -
#
# Todo:     -   -
#           -   -
#           -   -
#
# Version
#           (1.0) 2023-08-24    New created
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
import math

####################################################################
# Constants, Variables
#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5 # 25
SHORT_BREAK_MIN = 0.1 # 5
LONG_BREAK_MIN = 0.2 # 20

reps = 0
countdownid = None

###################################################################
# Functions
#
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(countdownid)
    reps = 0
    button_start.config(state="active")
    label_status.config(text="Timer")
    canvas.itemconfig( text_timer, text="00:00" )
    label_repeats.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    button_reset.config(state="active")
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    button_start.config(state="disabled")

    if reps % 8 == 0:
        label_status.config(text="L Break", fg=RED)
        countdown(long_break_seconds)
        reps=0
    elif reps % 2 == 0:
        label_status.config(text="S Break", fg=PINK)
        countdown(short_break_seconds)
    else:
        label_status.config(text="Work", fg=GREEN)
        countdown(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    if count>0:
        global countdownid
        countdownid = window.after(1000, countdown, count-1)
        count_minutes = math.floor(count/60)
        count_seconds = count % 60
        if count_seconds < 10:
            count_seconds = f"0{count_seconds}"
        canvas.itemconfig( text_timer, text=f"{count_minutes}:{count_seconds}" )
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks +="✓"
            label_repeats.config(text=marks)



####################################################################
# Classes
#
####################################################################
# Main
#
#Creating a new window and configurations
window = tkinter.Tk()
window.title("Pomodoro Time Manager")
window.minsize(width=400, height=400)
window.config(padx=30, pady=30, bg=YELLOW)



# ---------------------------- UI SETUP ------------------------------- #
label_status = tkinter.Label(text="Timer", font=("Arial", 25, "bold" ), fg=GREEN, bg=YELLOW )
label_status.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="Day028_Time-Manager-Pomodoro.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100,142, text="00:00", fill="white", font="Courier 24 bold")
canvas.grid(column=1, row=1)

button_start = tkinter.Button(text="Start")
button_start.grid(column=0, row=2)
button_start.config(command = start_timer)
button_reset = tkinter.Button(text="Reset")
button_reset.grid(column=2, row=2)
button_reset.config(command = reset_timer)
button_reset.config(state="disabled")

label_repeats = tkinter.Label(text="", font=("Arial", 25, "bold" ), fg=GREEN, bg=YELLOW )
label_repeats.grid(column=1, row=2)



window.mainloop()
