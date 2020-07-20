# p30.py
# Kyle Garcia
# 6/29/2020
# Python 3.8.3
# Description: A program that if given two int values, return their sum. If two values are the same, then return double their sum.

def sumDouble(a, b):  # define function
    sum = a + b
    if a == b:  # if a and b are the same value than double the sum
        value = sum * 2
    else:  # otherwise the result is just a + b
        value = sum
    return value


int1 = int(input("Please enter integer 1: "))
int2 = int(input("Please enter integer 2: "))
value = sumDouble(int1, int2)
print(value)

'''

Please enter integer 1: 3
Please enter integer 2: 3
12

Please enter integer 1: 6
Please enter integer 2: 4
10


'''
