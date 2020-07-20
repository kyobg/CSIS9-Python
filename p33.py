# p33.py
# Kyle Garcia
# 6/29/20
# Python 3.8.3
# Description: Write a function named isTriangle that takes three integers as arguments,
#               and that returns either True or False, depending on whether you can or cannot form a triangle from sticks with the given lengths.

def isTriangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        return False
    else:
        return True


def main():
    side1 = int(input('Side 1 Length (Int): '))
    side2 = int(input('Side 2 Length (Int): '))
    side3 = int(input('Side 3 Length (Int): '))
    result = isTriangle(side1, side2, side3)
    print("You can form a Triangle with {}, {}, and {}: {}".format(side1, side2, side3, result))


main()

'''
Side 1 Length (Int): 3
Side 2 Length (Int): 4
Side 3 Length (Int): 5
You can form a Triangle with 3, 4, and 5: True

Side 1 Length (Int): 3
Side 2 Length (Int): 20
Side 3 Length (Int): 7
You can form a Triangle with 3, 20, and 7: False

'''
