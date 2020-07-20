# p29.py
# Kyle Garcia
# 6/29/2020
# Python 3.8.3
# Description: A function abs(num) which returns the absolute value of a number

def absolute(num):
    numerator = num ** 2  # square num so it is even if it is negative
    if num < 0:  # if num is negative so its the denominator
        denominator = num * -1
        abs = numerator/denominator
    elif num > 0:  # if num is positive so is its denominator
        denominator = num
        abs = numerator/denominator
    elif num == 0:  # if num is 0, no denominator, its just 0
        abs = 0
    return abs  # return abs as a value for absolute()


intgr = int(input("Please enter in an integer: "))
result = absolute(intgr)
print(result)


'''

Please enter in an integer: -17
17

Please enter in an integer: 0
0

Please enter in an integer: 6
6

'''
