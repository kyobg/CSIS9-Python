# p38_sortList.py
# Kyle Garcia
# 7/14/2020
# Python 3.8.3
# Description: A function that returns the sorted list if reverse is false,
#              and returns the sorted list in reverse if reverse is true.

list = [5, 1, 4, 3, 2]

reverse = input("Reverse List? True or False: ")  # user input for reverse

if reverse == "True":  # if reverse is 'True' set value to True
    reverse = True

if reverse == "False":  # if reverse is 'False' set value to False
    reverse = False


def sort(list, reverse):  # sort function
    for j in range(len(list)):
        for k in range(len(list) - 1):
            if list[k] > list[k + 1]:  # switch placement of numbers to sort from least to greatest
                placehold = list[k + 1]
                list[k + 1] = list[k]
                list[k] = placehold
                sorted = list

    if reverse is True:  # return the list in reversed order
        print(sorted[::-1])

    if reverse is False:  # return the list in proper order
        print(sorted)


sort(list, reverse)  # call function

'''
Reverse List? True or False: True
[5, 4, 3, 2, 1]

Reverse List? True or False: False
[1, 2, 3, 4, 5]

'''
