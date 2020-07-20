# debug.py
# Kyle Garcia
# 7/16/2020
# Python 3.8.3
# Description: Debug program midterm


# Debug/fix the following program so that it shows the indicated output


def isEven(num):  # should have a parameter
    if (num % 2 == 0):
        return True
    else:
        return False


def main():  # should call isEven, does not return anything
    num = int(input("Please enter a number: "))
    print("The number %i is even: %s" % (num, isEven(num)))


main()  # should be called first

'''
=== OUTPUT ===
>>>
Enter a number: 5
The number 5 is even: False
>>>
'''
