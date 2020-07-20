# p42_fileIOAndMedian.py
# Kyle Garcia
# 7/18/2020
# Python 3.8.3
# Description: Program that (1) writes a random number of numbers in a file,
#              then (2) opens the file and reads the numbers from it into a list,
#              then (3) sorts the list and shows it, and then finally (4) calculates the median.

from random import randint

randFile = open("randomNumbers.txt", "w")  # creates a text file called randomNumbers.txt
rndAmnt = randint(50, 55)

for i in range(rndAmnt):
    randFile.write(str(randint(0, 100)) + '\n')

randFile.close()  # closes the file "randomNumbers.txt", and saves it

randFile = open("randomNumbers.txt", "r")  # reads randomNumbers.txt
list = randFile.read().splitlines()  # splits the individual lines in the text file as a list
for i in range(len(list)):  # make each item in the list into an integer instead of a string
    list[i] = int(list[i])


def sortList(list):  # function to sort the random number list from the file
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j + 1] < list[j]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    print(list)
    return list


def calcMedian(list):  # function that tests if the total items in the list is odd or even for the median
    if len(list) % 2 != 0:
        x = int((rndAmnt + 1) / 2)
        median = list[x]
        print("The Median is", median)
    if len(list) % 2 == 0:
        x = int(rndAmnt / 2)
        y = int(x + 1)
        median = (list[x] + list[y]) / 2
        print("The Median is", median)


def main():  # main function to facilitate the order of the functions
    sortList(list)
    calcMedian(list)


main()


'''

[0, 1, 1, 1, 2, 4, 4, 10, 11, 14, 16, 18, 20, 20, 21, 22, 23, 24, 26, 27, 28, 31, 31, 38, 39, 40, 40, 41, 42, 44, 51, 51, 53, 57, 58, 62, 63, 64, 64, 65, 71, 72, 72, 73, 73, 74, 75, 82, 89, 90, 91, 91, 92, 93, 97]
The Median is 42


[0, 0, 0, 1, 1, 3, 4, 9, 11, 16, 22, 23, 24, 26, 27, 28, 33, 35, 35, 38, 38, 38, 46, 49, 52, 52, 53, 57, 58, 61, 62, 64, 68, 68, 68, 69, 71, 72, 80, 81, 82, 82, 83, 83, 84, 87, 88, 92, 94, 95, 98, 100]
The Median is 55.0

'''
