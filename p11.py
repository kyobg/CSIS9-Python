# p11.py
# Kyle Garcia
# 6/11/2020
# Python 3.8
# Description: A program to simulate the rock-paper-scissors.

R = 1; # rock
P = 2; # paper
S = 3; # scissors

# ================USER=====================================
print("Rock Paper Scissors")
userPick = input("Please select R, P, or S: ") # User inputs R, P, S

if userPick == "R" or userPick == "r": # Turn R into 0
     selection = 0;
     
elif userPick == "P" or userPick == "p": # Turn P into 1
     selection = 1;

elif userPick == "S" or userPick == "s": # Turn S into 2
     selection = 2;

else:
    print("Invalid Input");

selectName = ["Rock", "Paper", "Scissors"] # A list to print the strings depending on a value

player = selection # set player equal to selection

print("You selected %s!" %(selectName[selection]))

#==================COMPUTER================================

import random
comPick = random.randint(0,2) # Selects a random number for the computer

computer = comPick # set computer equal to 'comPick'

print("Computer selected %s!" %(selectName[comPick]))

#==================COMPARE=================================

# Player Wins

if player == 0 and computer == 2:
    print("-----> You win! Rock breaks Scissors")

elif player == 2 and computer == 1:
    print("-----> You win! Scissors cut Paper")

elif player == 1 and computer == 0:
    print("-----> You win! Paper covers Rock")

# Computer Wins

elif player == 2 and computer == 0:
    print("-----> You lose (◉ ╭╮ ◉), Rock breaks Scissors")

elif player == 1 and computer == 2:
    print("-----> You lose (◉ ╭╮ ◉), Scissors cut Paper")

elif player == 0 and computer == 1:
    print("-----> You lose (◉ ╭╮ ◉),  Paper covers Rock")   


# Tie

else:
     print("Tie!");
     
'''

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p11.py ====================
Rock Paper Scissors
Please select R, P, or S: P
You selected Paper!
Computer selected Rock!
-----> You win! Paper covers Rock
>>> 

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p11.py ====================
Rock Paper Scissors
Please select R, P, or S: R
You selected Rock!
Computer selected Scissors!
-----> You win! Rock breaks Scissors
>>>

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p11.py ====================
Rock Paper Scissors
Please select R, P, or S: P
You selected Paper!
Computer selected Scissors!
-----> You lose (◉ ╭╮ ◉), Scissors cut Paper
>>> 

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p11.py ====================
Rock Paper Scissors
Please select R, P, or S: S
You selected Scissors!
Computer selected Scissors!
Tie!
>>> 

'''






















