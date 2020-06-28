# p23.py
# Kyle Garcia
# 6/20/2020
# Python 3.8
# Description: A program that asks the user to input a sentence, and two letter that will be counted throughout the sentence.

sentence = input("Please input a sentence here: ")
let1 = input("Please input the first letter to search for: ")
let2 = input("Please input the second letter to search for: ")
sentenceUpper = sentence.upper()
let1count = 0
let2count = 0
let1 = let1.upper()
let2 = let2.upper()
X = len(sentence)

for index in range(0, X, 1):

    if sentenceUpper[index] == let1:
        let1count += 1
    if sentenceUpper[index] == let2:
        let2count += 1

print("Letters =", let1, "and", let2)
print("The letter {} occurs {} times and the letter {} occurs {} times".format(let1, let1count, let2, let2count))

'''
>>>
Please input a sentence here: Yes, I will input a sentence here.
Please input the first letter to search for: e
Please input the second letter to search for: n
Letters = E and N
The letter E occurs 6 times and the letter N occurs 3 times
>>>
'''
