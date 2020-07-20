# midtermShortFunctions.py
# Kyle Garcia
# 7/16/2020
# Python 3.8.3
# Description: (1) Write a function which takes 2 float PARAMETERS distance and time.
#              The functions computes and SHOWS the speed = distance/ time rounded
#              to 2 values to the right of the decimal point,
#              for example: speed = 634.16
#              (2) Wrtie a function which takes 2 PARAMETERS num1, num2.
#              The function then RETURNS the bigger of the 2 numbers

def speed(dist, time):
    spd = 0
    spd = dist / time
    return spd


def main():
    dist = float(input("Please enter a distance: "))
    time = float(input("Please enter a time: "))
    print("The average speed is %.2f" % (speed(dist, time)))
    print("==============================================================")


main()

# =========================================================================
# =========================================================================


def bigger(num1, num2):
    if num1 > num2:
        return num1
    if num2 > num1:
        return num2
    if num1 == num2:
        print("The two numbers are equal")


def main2():
    num1 = int(input("Please input a whole number: "))
    num2 = int(input("Please input another whole number: "))
    print("The larger number is {}".format(bigger(num1, num2)))


main2()

'''
Please enter a distance: 500
Please enter a time: 3
The average speed is 166.67
==============================================================
Please input a whole number: 4
Please input another whole number: 25
The larger number is 25
'''
