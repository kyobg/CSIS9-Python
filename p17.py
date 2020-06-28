# p17.py
# Kyle Garcia
# 6/12/2020
# Python 3.8
# Description: Program that reads in X whole numbers and outputs the sum of all positive numbers, negative numbers and the sum of both.

# While loop to repeat the entire process if 'Y' is selected
while True:

    # User inputs number of numbers here
    numbers = int(input("How many numbers would you like to enter? "));


    negSum = 0;
    posSum = 0;
    totalSum = 0;

    # for loop to compute summed value of negative numbers and positive numbers
    for k in range(1,numbers+1,1):
        numValue = int(input("Please enter a value: "));
        if numValue > 0:
            posSum += numValue;

        if numValue < 0:
            negSum += numValue;

    # sum of both negSum and posSum
    totalSum = negSum + posSum;

    # Print the values calculated
    print("Positive Number Sum =",posSum);
    print("Negative Number Sum =", negSum);
    print("Total Sum =", totalSum);

    # Another for loop to make sure that 'Y' or 'N' is the input below
    while True:

        repeat = input("Would you like to repeat? [Y/N] ");
        repeat = repeat.upper();
    
        if repeat == "Y" or repeat == "YES":
            break; # this break terminates the while loop, thus returning back to the top of the program

        elif repeat == "N" or repeat == "NO":
            exit(); # exit program if repeat equals N or NO

        else: 
            continue; # this continue is to repeat the input for 'repeat'

    
'''

===================== RESTART: C:/Users/kyle/Desktop/p17.py ====================
How many numbers would you like to enter? 5
Please enter a value: -10
Please enter a value: 57
Please enter a value: 3
Please enter a value: 2
Please enter a value: -4
Positive Number Sum = 62
Negative Number Sum = -14
Total Sum = 48
Would you like to repeat? [Y/N] Y
How many numbers would you like to enter? 2
Please enter a value: 5
Please enter a value: -5
Positive Number Sum = 5
Negative Number Sum = -5
Total Sum = 0
Would you like to repeat? [Y/N] 

'''


