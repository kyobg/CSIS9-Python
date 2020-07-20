# p26.py
# Kyle Garcia
# 6/20/2020
# Python 3.8
# Description: Program to simulate 1000 students opening 1000 lockers in a particular fashion, and then return what lockers are open


# Variable values
lockers = 1000
lockerList = []
openLockers = 0
closedLockers = 0
incr = 0

for i in range(lockers + 1):
    lockerList.append(1)  # set each section in the list equal to 1

for j in range(lockers + 1):
    incr += 1  # increase the increment by one in each loop
    for k in range(0, lockers + 1, incr):
        if lockerList[k] == 1:  # if the locker is closed, then open it
            lockerList[k] = 0
        elif lockerList[k] == 0:  # else if, the locker is open, then close it
            lockerList[k] = 1
    lockerList[0] = 1  # locker 1 is always open

for m in range(lockers + 1):
    if lockerList[m] == 0:  # if the loop finds any zeroes in the list, add 1 to openLockers
        openLockers += 1
        print("Locker {} is Open".format(m))  # print if the locker is open
    else:
        closedLockers += 1  # count the amount of lockers that are closed

print("A total of {} Lockers are Open".format(openLockers))  # print the total amount of open lockers

'''

Locker 1 is Open
Locker 4 is Open
Locker 9 is Open
Locker 16 is Open
Locker 25 is Open
Locker 36 is Open
Locker 49 is Open
Locker 64 is Open
Locker 81 is Open
Locker 100 is Open
Locker 121 is Open
Locker 144 is Open
Locker 169 is Open
Locker 196 is Open
Locker 225 is Open
Locker 256 is Open
Locker 289 is Open
Locker 324 is Open
Locker 361 is Open
Locker 400 is Open
Locker 441 is Open
Locker 484 is Open
Locker 529 is Open
Locker 576 is Open
Locker 625 is Open
Locker 676 is Open
Locker 729 is Open
Locker 784 is Open
Locker 841 is Open
Locker 900 is Open
Locker 961 is Open
A total of 31 Lockers are Open

'''
