# p19.py
# Kyle Garcia
# 6/13/2020
# Python 3.8
# Description: A Dice Game program that generates two random values between 1 and 6 for you and 2 for the computer.

import random
import time
import os

print("==========DICE===========")
pDice = [random.randint(1,6),random.randint(1,6)]
cDice = [random.randint(1,6),random.randint(1,6)]

pTotal = pDice[0] + pDice[1]
cTotal = cDice[0] + cDice[1]

print("\nYou rolled %s and %s (Total: %s)\n" %(pDice[0],pDice[1],pTotal))

while True:
    reroll = input("Would you like to roll again? [Y/N] ")
    reroll = reroll.upper()
    if reroll not in ['N','NO','Y','YES']:
        print("\nPlease enter Y or N.\n")
        continue
    if reroll in ['N','NO']:
        print("\nThe Computer Rolled %s, You rolled %s" %(cTotal,pTotal))
        if cTotal > pTotal:
            print("You Lost...")
        elif cTotal < pTotal:
            print("You Win!!!")
        else:
            print("Tie")
        break
    else:
        pDice = [random.randint(1,6),random.randint(1,6)]
        pTotal = pDice[0] + pDice[1]
        print("\nYou rolled %s \n" %pTotal)
        continue
        
'''

>>> 
==================== RESTART: C:/Users/kyle/Desktop/p19.2.py ===================
==========DICE===========

You rolled 3 and 2 (Total: 5)

Would you like to roll again? [Y/N] y

You rolled 8 

Would you like to roll again? [Y/N] n

The Computer Rolled 4, You rolled 8
You Win!!!
>>>

>>> 
=============== RESTART: C:/Users/kyle/Desktop/p19.2.py ===============
==========DICE===========

You rolled 2 and 2 (Total: 4)

Would you like to roll again? [Y/N] Y

You rolled 4 

Would you like to roll again? [Y/N] Y

You rolled 8 

Would you like to roll again? [Y/N] s

Please enter Y or N.

Would you like to roll again? [Y/N] N

The Computer Rolled 10, You rolled 8
You Lost...
>>> 

>>> 
=============== RESTART: C:/Users/kyle/Desktop/p19.2.py ===============
==========DICE===========

You rolled 3 and 5 (Total: 8)

Would you like to roll again? [Y/N] n

The Computer Rolled 8, You rolled 8
Tie
>>> 

'''
