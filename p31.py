# p31.py
# Kyle Garcia
# 6/29/20
# Python 3.8.3
# Description: A program that takes two integers, n and m and returns true if n is evenly divisible by m and false otherwise.

def isDivisible(n, m):
    if (n % m) == 0:
        bool = True
    elif (n % m) != 0:
        bool = False
    return bool


int1 = int(input("Please input dividend: "))
int2 = int(input("Please input divisor: "))
boolean = isDivisible(int1, int2)
print("%i is evenly divisible by %i: %s" % (int1, int2, boolean))

'''

Please input dividend: 8
Please input divisor: 2
8 is evenly divisible by 2: True

Please input dividend: 57
Please input divisor: 4
57 is evenly divisible by 4: False

'''
