# p6.py
# Kyle Garcia
# 6/9/2020
# Python 3.8
# Description: Program to compute a person's height

# ask the user for the height, feet and inches
feet = int(input("Please input height feet (Whole Number): "));
print("Obtained! %i" %feet, "feet");
inches = int(input("Please input height inches (Whole Number)"));
print("Obtained! %i" %inches, "inches")

totalHeight = (feet * 12) + inches; # calculate total inches

if (inches > 1):         #  This if/else statement is for the word
    inchWord = "inches"; # inch or inches, it is just there so we can
else:                    # avoid using "inch(es)" in the wording 
    inchWord = "inch";
    

print("%i feet and %i %s = %i %s" %(feet, inches, inchWord, totalHeight, inchWord))
# show results

'''

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p6.py =====================
Please input height feet (Whole Number): 6
Obtained! 6 feet
Please input height inches (Whole Number)1
Obtained! 1 inches
6 feet and 1 inch = 73 inches
>>>

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p6.py =====================
Please input height feet (Whole Number): 6
Obtained! 6 feet
Please input height inches (Whole Number)2
Obtained! 2 inches
6 feet and 2 inches = 74 inches
>>> 

'''
