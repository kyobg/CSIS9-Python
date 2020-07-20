# p28.py
# Kyle Garcia
# 6/22/2020
# Python 3.8
# Description: Program to show all the prime numbers between 3 and 100

for i in range(3, 100, 1):
    for j in range(2, i):
        if (i % j == 0):  # when the number is not prime, break the second loop and go back to first loop.
            break
        if (i % j != 0 and j == i - 1):  # if the remainder is not 0, and the divisor is one less than 1, its a prime number. j == i - 1 ensures multiple
            print(i, "is prime")         # ^^^ messages aren't printed
'''

3 is prime
5 is prime
7 is prime
11 is prime
13 is prime
17 is prime
19 is prime
23 is prime
29 is prime
31 is prime
37 is prime
41 is prime
43 is prime
47 is prime
53 is prime
59 is prime
61 is prime
67 is prime
71 is prime
73 is prime
79 is prime
83 is prime
89 is prime
97 is prime

'''
