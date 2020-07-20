# p32.py
# Kyle Garcia
# 6/29/2020
# Python 3.8.3
# Description: Write a function called multAdd that takes three floats(a,b,c) as parameters and then returns a*b+c.
#               Write a main() function which starts the program, and calls the multAdd function giving it arguments 1,2,3.

def multAdd(a, b, c):  # define multAdd
    return (a * b) + c


def main():  # define main()
    a = 1
    b = 2
    c = 3
    print(multAdd(a, b, c))


# Input Values
a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))


value = multAdd(a, b, c)  # input parameters a, b, and c
print(value)
main()


'''

First number: 6
Second number: 5
Third number: 7
37.0
5

First number: 10
Second number: 10
Third number: 8
108.0
5

'''
