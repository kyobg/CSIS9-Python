# p14.py
# Kyle Garcia
# 6/11/2020
# Python 3.8
# Description: Program that askes the user for their day and month of a birhday
#               The Program then tells the zodiac signs that will be compatible
#               with that birthday

month = int(input("Please input the month of your birthday: "));
day = int(input("Please input the day of your birthday: "));

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("You are Aries, Fire group, compatible with Aries, Leo, and Sagittarius")

if (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("You are Taurus, Earth group, compatible with Taurus, Virgo, Capricorn")

if (month == 5 and day >= 21) or (month == 6 and day <= 21):
    print("You are Gemini, Air group, compatible with Gemini, Libra, Aquarius")

if (month == 6 and day >= 22) or (month == 7 and day <= 22):
    print("You are Cancer, Water group, compatible with Cancer, Scorpio, Pisces")

if (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("You are Leo, Fire group, compatible with Leo, Aries, Sagittarius")

if (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("You are Virgo, Earth group, compatible with Virgo, Taurus, Capricorn")

if (month == 9 and day >= 23) or (month == 10 and day <= 23):
    print("You are Libra, Air group, compatible with Libra, Gemini, Aquarius")

if (month == 10 and day >= 24) or (month == 11 and day <= 21):
    print("You are Scorpio, Water group, compatible with Scorpio, Cancer, Pisces")

if (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("You are Sagittarius, Fire group, compatible with Sagittarius, Aries, Leo")

if (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("You are Capricorn, Earth group, compatible with Capricorn, Virgo, Taurus")

if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("You are Aquarius, Air group, compatible with Aquarius, Libra, Gemini")

if (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("You are Pisces, Water group, compatible with Pisces, Cancer, Scorpio")

    
'''

>>> 
===================== RESTART: C:/Users/kyle/Desktop/p14.py ====================
Please input the month of your birthday: 9
Please input the day of your birthday: 17
You are Virgo, Earth group, compatible with Virgo, Taurus, Capricorn
>>> 
===================== RESTART: C:/Users/kyle/Desktop/p14.py ====================
Please input the month of your birthday: 7
Please input the day of your birthday: 3
You are Cancer, Water group, compatible with Cancer, Scorpio, Pisces
>>> 

'''
