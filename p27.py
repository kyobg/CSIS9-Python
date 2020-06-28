# p27.py
# Kyle Garcia
# 6/20/2020
# Python 3.8
# Description: Program that outputs as much stars as the variable numStars indicates.

numStars = int(input("How many stars (per row) would you like to display? "))

for i in range(numStars + 1):  # loops in range of numStars + 1
    for j in range(i):  # loop with respect to i
        print("*", end=' ')  # print '*' i number of times
    print()  # start a new line

'''

How many stars (per row) would you like to display? 12

*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *
* * * * * * * * * * *
* * * * * * * * * * * *

'''
