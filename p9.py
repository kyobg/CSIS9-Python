# p9.py
# Kyle Garcia
# 6/10/2020
# Python 3.8
# Description: Program to compute a person's height and print out a message.

print("Please enter your height");
feet = int(input("Feet: "));
inches = int(input("Inches: "));

totalInches = feet * 12 + inches; # Calculated the total height in inches

if totalInches > 72: # if totalInches is greater than 72, selection for tall height
    print("You are tall");
if totalInches >= 60 and totalInches <= 72: # if totalInches is less/equal 72 but greater/equal to 60, selection for average height
    print("You are average");
if totalInches < 60:             # if totalInches is less than 60, selection for vertically challenged
    print("You are vertically challenged");


'''

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p9.py =====================
Please enter your height
Feet: 6
Inches: 2
You are tall
>>> 

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p9.py =====================
Please enter your height
Feet: 4
Inches: 11
You are vertically challenged
>>>

'''
