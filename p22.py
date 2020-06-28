# p22.py
# Kyle Garcia
# 6/16/2020
# Python 3.8
# Description: Program that calculates the sum, minimum, maximum, and average of X amount of random numbers utilizing lists.

X = int(input("\nHow many numbers would you like to enter into a list? "))  # amount of numbers input
numList = []  # create an empty list

for num in range(0, X, 1):  # for loop for repeating number value input
    numInput = int(input("Please Input A Number: "))
    numList.append(numInput)  # add number to the end of the list

#  functions:


def Sum(X):  # function to sum the numbers of the list, argument is X

    added = 0

    for r in range(0, X, 1):  # for loop, repeat X amount of times
        added += numList[r]  # add all the numbers in numList together

    return added  # return the value of added


def great(X):  # function to find the greatest number within the list, argument is X

    maximum = numList[0]

    for r in range(0, X, 1):  # loop X amount of times

        if maximum < numList[r]:  # if the maximum is less than the current number...
            maximum = numList[r]  # ...set maximum equal to the current number

    return maximum  # return value of maximum


def less(X):  # function to find the smallest number within the list, argument is X

    minimum = numList[0]

    for r in range(0, X, 1):  # loop X amount of times

        if minimum > numList[r]:  # if the minimum is less than the current number...
            minimum = numList[r]  # ... set minimum equal to the current number

    return minimum  # return value of maximum


def average(X):  # function to find the average of all the numbers in the list

    average = Sum / X  # compute the average

    return average  # return the value of average


def twice(X):  # function to double the values in numList
    twoTimesList = []  # create an empty list
    for r in range(0, X, 1):  # loop X amount of times, to append a value to the list
        twoTimesList.append(0)
    for r in range(0, X, 1):  # loop X amount of times, to set each appended value equal to double the amount of numList[...]
        twoTimesList[r] = 2 * numList[r]
    return twoTimesList  # return the value of twoTimesList


def reversed(X):  # function to reverse the order of the doubled list
    reverseList = []  # create an empty list
    for r in range(0, X, 1):  # loop X amount of times to append
        reverseList.append(0)
    for r in range(X, 0, -1):  # loop in a decrement, to set the values in there position
        i = X - r
        reverseList[i] = twice[r - 1]
    return reverseList  # return value of reverseList

#  set variables equal to the functions


Sum = Sum(X)
maximum = great(X)
minimum = less(X)
average = average(X)
twice = twice(X)
reversed = reversed(X)


# print all the values
print(numList)
print("\nThe Sum is: {}\nThe Maximum is: {}\nThe Minimum is: {}\nThe Average is: {}\n".format(Sum, maximum, minimum, average))
print("\n")
print("The doubled version of the list is:\n{}".format(twice))
print("\n")
print("The reversed version of the doubled list is:\n{}".format(reversed))

'''
How many numbers would you like to enter into a list? 6
Please Input A Number: 60
Please Input A Number: 60
Please Input A Number: 24
Please Input A Number: 365
Please Input A Number: 19
Please Input A Number: 2020
[60, 60, 24, 365, 19, 2020]

The Sum is: 2548
The Maximum is: 2020
The Minimum is: 19
The Average is: 424.6666666666667



The doubled version of the list is:
[120, 120, 48, 730, 38, 4040]


The reversed version of the doubled list is:
[4040, 38, 730, 48, 120, 120]
>>>
How many numbers would you like to enter into a list? 11
Please Input A Number: 3
Please Input A Number: 6
Please Input A Number: 1
Please Input A Number: 2
Please Input A Number: 12
Please Input A Number: 13
Please Input A Number: 19
Please Input A Number: 20
Please Input A Number: 17
Please Input A Number: 2
Please Input A Number: 1
[3, 6, 1, 2, 12, 13, 19, 20, 17, 2, 1]

The Sum is: 96
The Maximum is: 20
The Minimum is: 1
The Average is: 8.727272727272727



The doubled version of the list is:
[6, 12, 2, 4, 24, 26, 38, 40, 34, 4, 2]


The reversed version of the doubled list is:
[2, 4, 34, 40, 38, 26, 24, 4, 2, 12, 6]
>>>
'''
