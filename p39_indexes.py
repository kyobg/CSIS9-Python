# p39_indexes.py
# Kyle Garcia
# 7/14/2020
# Python 3.8.3
# Description: A function that takes a list and an item, then returns a list of indexes
#              where the item was found.

list = ['one', 'two', 'two', 'three', 'two', 'four', 'one', 'five', 'two']


def indexes(list, item):
    tempList = []  # temporary empty list
    for i in range(len(list)):
        if list[i] == 'two':  # if list[i] is equal to the word we are looking for...
            tempList += [i]  # add that position number to tempList
    return tempList  # return the list values


print(indexes(list, 'two'))  # call function, searching for the word 'two'

'''
[1, 2, 4, 8]

'''
