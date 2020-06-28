# p14.py
# Kyle Garcia
# 6/11/2020
# Python 3.8
# Description: Program that askes the user for their day and month of a birhday
#               The Program then tells the zodiac signs that will be compatible
#               with that birthday

month = int(input("Please input the month of your birthday: ")); # input for bday month
day = int(input("Please input the day of your birthday: ")); # input for bday day

# lists for group compatibilities

fire = ["Aries", "Leo", "Sagittarius"];
water = ["Pisces", "Cancer", "Scorpio"];
earth = ["Taurus", "Virgo", "Capricorn"];
air = ["Aquarius", "Libra", "Gemini"];

#=======================Zodiac Selection============================

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    zodiac = "Aries" # name for zodiac
    group = "Fire"   # name for group
    compat = fire    # name for group compatibility
    
if (month == 4 and day >= 20) or (month == 5 and day <= 20):
    zodiac = "Taurus"
    group = "Earth"
    compat = earth
    
if (month == 5 and day >= 21) or (month == 6 and day <= 21):
    zodiac = "Gemini"
    group = "Air"
    compat = air
    
if (month == 6 and day >= 22) or (month == 7 and day <= 22):
    zodiac = "Cancer"
    group = "Water"
    compat = water
    
if (month == 7 and day >= 23) or (month == 8 and day <= 22):
    zodiac = "Leo"
    group = "Fire"
    compat = fire
    
if (month == 8 and day >= 23) or (month == 9 and day <= 22):
    zodiac = "Virgo"
    group = "Earth"
    compat = earth
    
if (month == 9 and day >= 23) or (month == 10 and day <= 23):
    zodiac = "Libra"
    group = "Air"
    compat = air
    
if (month == 10 and day >= 24) or (month == 11 and day <= 21):
    zodiac = "Scorpio"
    group = "Water"
    compat = water
    
if (month == 11 and day >= 22) or (month == 12 and day <= 21):
    zodiac = "Sagittarius"
    group = "Fire"
    compat = fire
    
if (month == 12 and day >= 22) or (month == 1 and day <= 19):
    zodiac = "Capricorn"
    group = "Earth"
    compat = earth
    
if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    zodiac = "Aquarius"
    group = "Water"
    compat = water
    
if (month == 2 and day >= 19) or (month == 3 and day <= 20):
    zodiac = "Pisces"
    group = "Water"
    compat = water

#======================Return Message=============================

compat = ', '.join(compat) # turns the list into a joined string 'word1, word2, word3'
print("You are %s, %s group, compatible with %s" %(zodiac, group, compat)); # show message for sign

'''

>>> 
==================== RESTART: C:/Users/kyle/Desktop/p14.2.py ===================
Please input the month of your birthday: 9
Please input the day of your birthday: 17
You are Virgo, Earth group, compatible with Taurus, Virgo, Capricorn
>>> 
==================== RESTART: C:/Users/kyle/Desktop/p14.2.py ===================
Please input the month of your birthday: 7
Please input the day of your birthday: 3
You are Cancer, Water group, compatible with Pisces, Cancer, Scorpio
>>> 

'''
