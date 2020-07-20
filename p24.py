# p24.py
# Kyle Garcia
# 6/20/2020
# Python 3.8
# Description: Program that displays the character sin the ASCII character table from ! to ~

print("ASCII TABLE\n==========================")
count = 0
for ascii in range(33, 127, 1):
    print(chr(ascii), end=' ')  # chr() returns a character in the ascii table
    count = count + 1
    if count == 10:
        print()
        count = 0
print("\n")

'''

ASCII TABLE
==========================
! " # $ % & ' ( ) *
+ , - . / 0 1 2 3 4
5 6 7 8 9 : ; < = >
? @ A B C D E F G H
I J K L M N O P Q R
S T U V W X Y Z [ \
] ^ _ ` a b c d e f
g h i j k l m n o p
q r s t u v w x y z
{ | } ~

'''
