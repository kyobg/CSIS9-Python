# p40_splitSentence.py
# Kyle Garcia
# 7/14/2020
# Python 3.8.3
# Description: A program that askes the user to enter a sentence, the program then
#              counts the words, shows the last word of the sentence, and then asks
#              the user to enter their own word, and count the amount in the sentence

sentence = input("Please enter a sentence: ")
wordList = sentence.split(" ")  # splits the sentence by spaces, then place into a list
length = len(wordList)  # var for length of created list


def wordTotal(sentence):  # function that returns the total amount of words in the sentence
    count = 0
    for i in range(len(wordList)):
        count += 1
    print("There are {} words in the sentence you entered.".format(count))


def wordLast(sentence):  # function that prints the last word of wordList
    print("The last word is '{}'".format(wordList[length - 1]))


def wordUser(sentence, word):  # function that searches for the amount of times the word entered is found
    userCount = 0
    for j in range(length):
        if wordList[j] == word:
            userCount += 1
    print("The word '{}' appears {} times.".format(word, userCount))


def main():  # function to put all the other functions under one, to clean up code
    wordTotal(sentence)
    wordLast(sentence)
    word = input("What word would you like to count? ")  # word input from user
    wordUser(sentence, word)


main()  # call the function main()


'''
Please enter a sentence: The fox and dog were running and jumping
There are 8 words in the sentence you entered.
The last word is 'jumping'
What word would you like to count? and
The word 'and' appears 2 times.
'''
