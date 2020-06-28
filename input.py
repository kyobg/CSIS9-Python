# input.py
# Kyle Garcia
# 6/9/2020
# Python 3.8
# Description: Program to take input in Python

name = input("Please enter your name: "); # this os a string
weightLbs = float(input("Please enter your weight in lbs: ")); # A float
age = int(input("Please enter your age (Whole Number): ")); # An Integer
weightKg = weightLbs * 0.453592;
title = "Human";

print("Hello, ", title, name, "your weight is")
print(weightLbs, "lbs")
print("which equals = %.2f" %weightKg, end = ' ') # end='' prevents a new line
print("kilograms")

'''

>>> 
==================== RESTART: C:/Users/kyle/Desktop/input.py ===================
Please enter your name: Kyle
Please enter your weight in lbs: 196
Please enter your age (Whole Number): 19
Hello,  Human Kyle your weight is
196.0 lbs
which equals = 88.90 kilograms
>>>

'''
