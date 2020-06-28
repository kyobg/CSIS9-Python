# p21.py
# Kyle Garcia
# 6/14/2020
# Python 3.8
# Description: Program that generates X random integers and calculates the smallest, largest, sum, and average of the numbers.
from random import randint

amnt = randint(10, 15)  # generate a random number
numbers = []

for X in range(0, amnt, 1):
    numbers.append(randint(20, 50))  # add random numbers in each list slot
    numString = str(numbers)
    numString = numString.replace('[', '').replace(']', '')  # removes the brackets from the list
print("\nList of Numbers = {}\n".format(numString))


def avgAndSum():  # function that finds the average and sum of the numbers
    added = numbers[0]
    for X in range(1, amnt, 1):
        added += numbers[X]  # compute the sum
        avg = (added / (X + 1))  # compute average
    print("Sum = {}\n".format(added))
    print("Average = {:.2f}\n".format(avg))


def smallAndLarge():  # function that finds the smallest number and the largest number

    small = numbers[0]

    for X in range(0, amnt, 1):
        if small > numbers[X]:  # comparison to see if the number[X] is smaller
            small = numbers[X]  # set smallest number equal to number[X] if it is smaller

    large = numbers[0]

    for X in range(0, amnt, 1):
        if large < numbers[X]:   # comparison to see if the number[X] is larger
            large = numbers[X]  # set largest number equal to number[X] if it is larger

    print("Smallest = {}\n".format(small))
    print("Largest = {}\n".format(large))


avgAndSum()  # run the function
smallAndLarge()  # run the function


'''

>>>
===================== RESTART: C:/Users/kyle/Desktop/p21.py ====================

List of Numbers = 30, 33, 26, 38, 38, 33, 34, 45, 50, 50

Sum = 377

Average = 37.70

Smallest = 26

Largest = 50

>>>

===================== RESTART: C:/Users/kyle/Desktop/p21.py ====================

List of Numbers = 24, 25, 44, 44, 50, 22, 41, 35, 24, 35, 21, 36

Sum = 401

Average = 33.42

Smallest = 21

Largest = 50

>>>

===================== RESTART: C:/Users/kyle/Desktop/p21.py ====================

List of Numbers = 33, 47, 28, 22, 32, 31, 34, 36, 45, 40, 30, 40

Sum = 418

Average = 34.83

Smallest = 22

Largest = 47

>>>

'''
