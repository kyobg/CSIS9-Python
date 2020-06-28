# p16.py
# Kyle Garcia
# 6/12/2020
# Python 3.8
# Description: Program that computes the tuition in ten years and displays a table of the years and tuition costs

year = 0
tuition = 10000

print("Year:           Tuition Price \n==========================================") # print the header

while year < 10: # loop while year is less than 10
    year += 1; # increment year by 1
    if year > 1: # if the year is greater than 1...
        tuition = tuition * 1.05; # compute the increment of 5% for tuition per year
    print("Year: {:<2.0f}     Tuition: {:<2.0f} Dollars".format(year,tuition)); # print the columns in a format
                #  ^   ^ format, align to th left by 2, and remove decimal places

'''

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p16.py ====================
Year:           Tuition Price 
==========================================
Year: 1      Tuition: 10000 Dollars
Year: 2      Tuition: 10500 Dollars
Year: 3      Tuition: 11025 Dollars
Year: 4      Tuition: 11576 Dollars
Year: 5      Tuition: 12155 Dollars
Year: 6      Tuition: 12763 Dollars
Year: 7      Tuition: 13401 Dollars
Year: 8      Tuition: 14071 Dollars
Year: 9      Tuition: 14775 Dollars
Year: 10     Tuition: 15513 Dollars
>>> 

'''
