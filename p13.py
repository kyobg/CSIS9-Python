# p13.py
# Kyle Garcia
# 6/11/2020
# Python 3.8
# Description: Program to convert any given number of total cents (under 100) into the correct number of: quarters, dimes, nickels, pennies.

totalCents = int(input("Please enter total cents: "))

quarters = int(totalCents/25);

if quarters > 0: # if there are any quarters

    print("You have", quarters, "Quarters"); # Tells the user how much quarters they have

    totalCents = totalCents - quarters*25;

dimes = int(totalCents/10);

if dimes > 0: # if there are any dimes

    print("You have", dimes, "Dimes"); # Tells the user how much dimes they have

    totalCents = totalCents - dimes*10;

nickels = int(totalCents/5);

if nickels > 0: # if there are any nickels
    
    print("You have", nickels, "Nickels"); # Tells the user how much nickels they have

    totalCents = totalCents - nickels*5;

pennies = int(totalCents/1);

if pennies > 0: # if there are any pennies
    
    print("You have", pennies, "Pennies"); # Tells the user how much pennies they have

    totalCents = totalCents - pennies;
    
'''

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p13.py ====================
Please enter total cents: 67
You have 2 Quarters
You have 1 Dimes
You have 1 Nickels
You have 2 Pennies
>>>

'''
