# p41_sunspots.py
# Kyle Garcia
# 7/18/2020
# Python 3.8.3
# Description: A program that reads the data from sunspots.txt and computes
#              computes the average for each year, writing them to a file averages.txt

import subprocess  # to open text file after

myFile = open('sunspots.txt', 'r')  # reads sunspots.txt
avgFile = open('averages.txt', 'w')  # allows writing/creates file for averages
listOfLines = myFile.read().splitlines()
avgList = []
yearList = []


def getYears(listOfLines):  # function to append the years to a list
    for i in range(len(listOfLines)):
        line = listOfLines[i].split()
        yearList.append(line[0])


def getAvg(listOfLines):  # function that splits the text file lines into a list
    for i in range(len(listOfLines)):
        average((listOfLines[i].split()))


def average(line):  # get the average of one year
    avg = 0
    for i in range(1, len(line)):
        avg += float(line[i])
    avg = avg / (len(line) - 1)
    avg = round(avg, 2)
    avgList.append(avg)  # add average of the year to the list avgList


def writeFile(yearList, avgList):  # function to write the Year and average to the file
    avgFile.write("Year     Average\n")
    for i in range(len(yearList)):
        avgFile.write(str(yearList[i]) + "     " + str(avgList[i]) + "\n")


getAvg(listOfLines)
getYears(listOfLines)
writeFile(yearList, avgList)
myFile.close()
avgFile.close()

try:
    subprocess.Popen(['notepad.exe', "averages.txt"])

except:
    pass
