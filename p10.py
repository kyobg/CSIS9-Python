# p10.py
# Kyle Garcia
# 6/11/2020
# Python 3.8
# Description: Program that askes the user for a student's grade as a percent and then returns their letter grade

grade = float(input("Please enter in a Percentage: ")); # user input for grade percentage

if grade < 0 or grade > 100: # validate user input
    print("Invalid percent entered, must be between 0 and 100");
    grade = float(input("Please enter in a Percentage: ")); # input for percentage
else:
    print(grade);

if grade <= 100 and grade >= 90: # if grade in between 100-90 ... "A"
    print('You have an "A"')

elif grade < 90 and grade >= 80: # if grade in between 90-80 ... "B"
    print('You have a "B"');

elif grade < 80 and grade >= 70: # if grade in between 80-70 ... "C"
    print('You have a "C"');

elif grade < 70 and grade >= 60: # if grade in between 70-60 ... "D"
    print('You have a "D"');

elif grade < 60 and grade >= 0: # if grade in between 60-0 ... "F"
    print('You have an "F"');

while grade < 0 or grade > 100: # this 'while' ensures that if an invalid number is input, the input is prompted again
    
    if grade < 0 or grade > 100: 
        print("Invalid percent entered, must be between 0 and 100");
        grade = float(input("Please enter in a Percentage: "));
    else:
        print(grade);

    if grade <= 100 and grade >= 90: 
        print('You have an "A"');

    elif grade < 90 and grade >= 80: 
        print('You have a "B"');

    elif grade < 80 and grade >= 70: 
        print('You have a "C"');

    elif grade < 70 and grade >= 60: 
        print('You have a "D"');

    elif grade < 60 and grade >= 0:
        print('You have an "F"');

'''

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p10.py ====================
Please enter in a Percentage: 120
Invalid percent entered, must be between 0 and 100
Please enter in a Percentage: -1
Invalid percent entered, must be between 0 and 100
Please enter in a Percentage: 100.000000001
Invalid percent entered, must be between 0 and 100
Please enter in a Percentage: 99.99999999
You have an "A"
>>> 

'''
