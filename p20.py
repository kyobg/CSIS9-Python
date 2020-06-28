# p20.py
# Kyle Garcia
# 6/14/2020
# Python 3.8
# Description: Program that lets child pratice their arithmetic skills

from random import randint
from time import sleep


def start():   # function that defines what we are picking

    pick = int(input("\nWould you like to add(1), subtract(2), or multiply(3): "))

    return pick   # function outputs value of 'pick'


def add():  # function that makes the entire addition process

    # get random integers
    rnd1 = randint(0, 9)
    rnd2 = randint(0, 9)
    added = (rnd1 + rnd2)  # add random integers together

    while True:  # while loop to repeat the question if answered incorrectly
        try:  # tries the code below...
            ans = int(input("\nWhat is {} + {} equal to? ".format(rnd1, rnd2)))

            if ans == added:  # if ans == added, print correct and delay retry() for 1 second
                print("\nCorrect!")
                sleep(1)
                retry()  # run retry function

            elif ans != added:  # if ans is not equal to added, repeat the while loop
                print("\nSorry, that is incorrect")
                sleep(1)
                continue

            break  # end while loop

        except ValueError:  # if the try has a value error..
            print("\nPlease input an integer")  # print string
            sleep(1)
            continue  # ....and repeat while loop for ans


def subtract():  # function that makes the entire subtraction process

    # get random integers
    rnd1 = randint(0, 9)
    rnd2 = randint(0, 9)
    diff = (rnd1 - rnd2)  # subtract rnd2 from rnd 1

    while True:  # while loop to repeat the question if answered incorrect
        try:  # tries code below...
            ans = int(input("\nWhat is {} - {} equal to? ".format(rnd1, rnd2)))

            if ans == diff:  # if true, print correct
                print("\nCorrect")
                sleep(1)
                retry()

            elif ans != diff:  # if true, print incorrect
                print("\nSorry, that is incorrect")
                sleep(1)
                continue  # repeat while loop

            break  # end while loop

        except ValueError:  # if an invalid input it said...
            print("\nPlease input an integer")  # ...print this statement...
            sleep(1)
            continue  # ... and repeat the while loop


def multiply():  # function for all the multiplication processes

    # get random integers
    rnd1 = randint(0, 9)
    rnd2 = randint(0, 9)
    product = rnd1 * rnd2  # multiply random integers

    while True:  # while loop for incorrect answers
        try:  # tries code below...
            ans = int(input("\nWhat is {} X {} equal to? ".format(rnd1, rnd2)))

            if ans == product:  # if ans == product...
                print("\nCorrect!")  # ...print correct...
                sleep(1)
                retry()  # ...and run retry()

            elif ans != product:  # if ans is not equal to product...
                print("\nSorry, that is incorrect")  # ...print statement...
                sleep(1)
                continue  # ... and repeat while loop
            break  # end while loop

        except ValueError:  # if an invalid input is said...
            print("\nPlease input an integer")
            sleep(1)
            continue  # ...repeat while loop


def retry():  # function that controls the try another statements

    while True:
        retry = input("\nWould you like to try another problem? [Y/N] ")
        retry = retry.upper()

        if retry in ['Y', 'YES']:  # if Y or Yes, end while loop
            break

        elif retry in ['N', 'NO']:  # else if N or NO exit program
            print("\nThanks for playing!")
            sleep(2)
            exit()

        else:  # else, repeat while loop
            print("\nPlease input a Y or N")
            sleep(2)
            continue


# Processes start here
while True:

    try:
        pick = start()  # set pick equal to the returned value of 'start()'
        if pick == 1:
            add()  # run add() function
            continue  # repeat while loop

        elif pick == 2:
            subtract()  # run subtract() function
            continue  # repeat while loop

        elif pick == 3:
            multiply()  # run multiply() function
            continue  # repeat while loop

    except ValueError:  # if invalid input...
        print("Please enter a 1, 2, or 3")  # ...print this...
        sleep(1)
        continue  # ...and repeat while loop


'''

==================== RESTART: C:/Users/kyle/Desktop/p20.2.py ===================

Would you like to add(1), subtract(2), or multiply(3): 1

What is 8 + 9 equal to? 17

Correct!

Would you like to try another problem? [Y/N] Y

Would you like to add(1), subtract(2), or multiply(3): 2

What is 8 - 7 equal to? 1

Correct

Would you like to try another problem? [Y/N] Y

Would you like to add(1), subtract(2), or multiply(3): 3

What is 4 X 7 equal to? 28

Correct!

Would you like to try another problem? [Y/N] h

Please input a Y or N

Would you like to try another problem? [Y/N] Y

Would you like to add(1), subtract(2), or multiply(3): 2

What is 5 - 9 equal to?

Please input an integer

What is 5 - 9 equal to? 3

Sorry, that is incorrect

What is 5 - 9 equal to? 2

Sorry, that is incorrect

What is 5 - 9 equal to? -4

Correct

Would you like to try another problem? [Y/N] Y

Would you like to add(1), subtract(2), or multiply(3): 1

What is 9 + 2 equal to? 10

Sorry, that is incorrect

What is 9 + 2 equal to? 11

Correct!

Would you like to try another problem? [Y/N] Y

Would you like to add(1), subtract(2), or multiply(3): 3

What is 8 X 0 equal to? 1

Sorry, that is incorrect

What is 8 X 0 equal to? h

Please input an integer

What is 8 X 0 equal to? 0

Correct!

Would you like to try another problem? [Y/N] h

Please input a Y or N

Would you like to try another problem? [Y/N] N

Thanks for playing!

'''
