#!/usr/bin/env python3
####################################################################
#           - Day009_Blind-Auction.py -
#
# Copyright (C) 2023 holgihe <holgihe@gmx.net>
#
####################################################################
# Part of:  Udemy Course -100 Days of Code Python - Angela Yu
#
# Synopse:  Several participants can enter their name and bid value US$.
##             Program then output the winner
# Input:    - name
#           - bid value (US$)
# Output:   - Highest bidder (name, amount),
#           -
#
# Todo:
#
# Version   (1.0) 2023-03-25    New created
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

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Import os module
import os

def clear():
    # Check if Operating System is Mac and Linux or Windows
   print(os.name)
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

clear()
print(logo)
print("Welcome to the secret auction program.")

def get_bid():
   name = input("What is Your name ?  ")
   bid  = int(input("What's Your bid ?    $"))
   bids[name] = bid

def ask_other_bids():
  other_bidders = input("Are there any others biders ? Type 'yes' or 'no' ")
  if other_bidders == 'yes':
    clear()
    return(1)
  elif other_bidders == 'no':
    clear()
    return(0)
bids = {}

def find_highest_bider(bidding_record):
  highest_amount = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_amount:
      highest_amount = bid_amount
      winner = bidder
  print(f"The Winner is {winner} with a bid of US${highest_amount}")

#============================================
#Main programm
nextbidder = 1
while nextbidder:
  get_bid()
  nextbidder = ask_other_bids()
find_highest_bider(bids)
