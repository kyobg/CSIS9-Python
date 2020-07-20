# midtermLongerProgram.py
# Kyle Garcia
# 7/16/2020
# Python 3.8.3
# Description: A program to find the traits of a triangle from 3 given lengths

from time import sleep


def main():
    A = int(input("Please input the length of side one (Whole Number): "))
    B = int(input("Please input the length of side two (Whole Number): "))
    C = int(input("Please input the length of side three (Whole Number): "))

    while True:
        if (A < 0) or (B < 0) or (C < 0):
            print("Please Input Positive Value\n")
            if A < 0:
                A = int(input("Please input the length of side one (Whole Number): "))
            if B < 0:
                B = int(input("Please input the length of side two (Whole Number): "))
            if C < 0:
                C = int(input("Please input the length of side three (Whole Number): "))
        else:
            break
    isTriangle(A, B, C)
    triangleType(A, B, C)


def isTriangle(A, B, C):
    if (A >= B + C) or (B >= A + C) or (C >= A + B):
        print("The three values cannot create a triangle")


def triangleType(A, B, C):
    if A == B and A == C:
        print("The triangle is Equilateral")
    elif (A**2 + B**2 == C**2) or (B**2 + C**2 == A**2) or (A**2 + C**2 == B**2):
        print("The triangle is a Right Triangle")
    elif (A == B and A != C) or (B == C and B != A) or (A == C and A != B):
        print("The triangle is Isoceles")
    elif (A >= B + C) or (B >= A + C) or (C >= A + B):
        pass
    else:
        print("The triangle is Another type (Scalene)")


while True:
    main()
    repeat = input("Would you like to repeat? (Y/N) ")
    repeat = repeat.upper()
    if repeat in ["Y", "YES"]:
        continue
    elif repeat in ["N", "NO"]:
        break
    else:
        print("A improper response was entered, stopping program anyways...")
        sleep(3)
        break

'''
Please input the length of side one (Whole Number): 3
Please input the length of side two (Whole Number): 4
Please input the length of side three (Whole Number): 5
The triangle is a Right Triangle
Would you like to repeat? (Y/N) y
Please input the length of side one (Whole Number): 3
Please input the length of side two (Whole Number): 3
Please input the length of side three (Whole Number): 3
The triangle is Equilateral
Would you like to repeat? (Y/N) Y
Please input the length of side one (Whole Number): 2
Please input the length of side two (Whole Number): 2
Please input the length of side three (Whole Number): 3
The triangle is Isoceles
Would you like to repeat? (Y/N) Y
Please input the length of side one (Whole Number): 356
Please input the length of side two (Whole Number): 333
Please input the length of side three (Whole Number): 1000
The three values cannot create a triangle
The triangle is Another type (Scalene)
Would you like to repeat? (Y/N) Y
Please input the length of side one (Whole Number): 3
Please input the length of side two (Whole Number): 5
Please input the length of side three (Whole Number): 6
The triangle is Another type (Scalene)
Would you like to repeat? (Y/N) N
'''
