# p7.py
# Kyle Garcia
# 6/9/2020
# Python 3.8
# Description: Program to compute the circumference and area of a circle.

pi = 3.1415
print("________________________________________________________________\n")
print("Circumference and Area of a Circle")
print("________________________________________________________________\n")

radius = float(input("What is the radius (in inches) of the circle that you want to draw?  "))
# ^^ask user for radius input
area = pi * radius ** 2 # compute area
circumference = 2 * pi * radius # compute circumference

if (radius == 1):          #  if/else statement is for changing
    inchWord = "inch";     # the word inch to inch or inches depending
else:                      # on the radius value
    inchWord = "inches";

print("A circle with a radius of %.1f %s has \n Circumference: %.1f inches \n Area: %.1f square inches" %(radius,inchWord,circumference,area))
# show results back to user


'''

>>>
===================== RESTART: C:/Users/kyle/Desktop/p7.py =====================
________________________________________________________________

Circumference and Area of a Circle
________________________________________________________________

What is the radius (in inches) of the circle that you want to draw?  1
A circle with a radius of 1.0 inch has
 Circumference: 6.3 inches
 Area: 3.1 square inches
>>>

'''
