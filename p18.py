# p18.py
# Kyle Garcia
# 6/13/2020
# Python 3.8
# Description: Program that calculates exactly how much more or less you can make with the penny on day 30.

# set values for variables
penny = 1
day = 0

# print header message
print("Which gives you more money?")
print("#1. A penny which doubles it's value over 30 days")
print("#2. A million dollars on day 1")
print("======================================================\n")

# for loop for 'day' for 0 to 30 incrementing by 1
for day in range(0,30,1):
    if day > 0: # if day is greater than 0, penny = penny * 2
        penny *= 2
    message = "{:,}".format(penny) # format for comma separators in big numbers

print("1,000,000 Dollars Day One\n") # Print 1 million dollars
print("Penny on day thirty = {:,} Dollars\n".format(penny)) # format comma separators

difference = penny - 1000000 # calculate the difference between 1 mil day one and 30 day penny

print("The difference between the two = {:,} Dollars".format(difference)) # comman separators for 'difference'


'''

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p18.py ====================
Which gives you more money?
#1. A penny which doubles it's value over 30 days
#2. A million dollars on day 1
======================================================

1,000,000 Dollars Day One

Penny on day thirty = 536,870,912 Dollars

The difference between the two = 535,870,912 Dollars
>>> 

'''
