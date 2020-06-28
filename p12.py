# p12.py
# Kyle Garcia
# 6/11/2020
# Python 3.8
# Description: Program to determine if the user can vote.

# ask user for input

age = int(input("How old are you? "))
citizen = input("Are you a citizen? (y/n): ")
vote = input("Have you registered to vote? (y/n): ")

# if they can vote

if age >= 18 and citizen in ["y","Y"] and vote in ["Y","y"]: # the 'in' [] is for caps and lowercase
    print("Congratulations you can vote!");

# if they cannot vote

else:
    
    print("Sorry you cannot vote");

    if age < 18:
        print("-> You are not old enough");

    if citizen not in ['y','Y']:
        print("-> You must be a citizen");

    if vote not in ['y','Y']:
        print("-> You must be registered");

'''

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p12.py ====================
How old are you? 1
Are you a citizen? (y/n): n
Have you registered to vote? (y/n): n
Sorry you cannot vote
-> You are not old enough
-> You must be a citizen
-> You must be registered
>>> 
===================== RESTART: C:/Users/kyle/Desktop/p12.py ====================
How old are you? 17
Are you a citizen? (y/n): y
Have you registered to vote? (y/n): n
Sorry you cannot vote
-> You are not old enough
-> You must be registered
>>> 
===================== RESTART: C:/Users/kyle/Desktop/p12.py ====================
How old are you? 19
Are you a citizen? (y/n): y
Have you registered to vote? (y/n): y
Congratulations you can vote!
>>> 

'''
