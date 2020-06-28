# output.py
# Kyle Garcia
# 6/8/2020
# Python 3.8
# Description: Program to show output in Python

print('hello world') # single quote
print("hello world") # double quote
print("he/nllo") # /n insert a new line (same as pressing Enter)

# VARIABLES are named storage locations for numbers, strings, lists
# STRING is anything enclosed in quotes "Hello World", that's a string
# NUMBER can be either a FLOAT (Ex: 9.3) or an INTEGER (Ex: 9.0)
# LISTS are things like [1,2,3] or ["Kyle", "Garcia"]
myName = "Kyle" # declare/initialize string variable myName
Weight = 194.2743 # declare/initialize float variable Weight
Age = 19 # declare/initialize int variable Age
Grades = [90,77,88]
nameZ = ["Kyle", "Garcia"]

print ("Hello ", myName)
print ("Your weight is ", Weight, " and your age is ", Age)
print ("Your weight is %.2f and your age is %i" %(Weight,Age))
print ("Lists: grades=", Grades, "nameZ=",nameZ)
print ("This is how you print", end = ' ')
print ("on the same line")


'''
>>> 
=================== RESTART: C:/Users/kyle/Desktop/output.py ===================
hello world
hello world
he/nllo
Hello  Kyle
Your weight is  194.2743  and your age is  19
Your weight is 194.27 and your age is 19
Lists: grades= [90, 77, 88] nameZ= ['Kyle', 'Garcia']
This is how you print on the same line
>>> 
'''

