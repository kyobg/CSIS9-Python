# p43_dataMining.py
# Kyle Garcia
# 7/21/2020
# Python 3.8.3
# Description: Program that calculates the average of each month of every year.

# name: get_data_list
# param: FILE_NAME  - the file's name you saved for the stock's prices
# brief: get a list of the stock's records' lists
# return: a list of lists

def get_data_list(FILE_NAME):
    file = open(FILE_NAME, "r")
    data_list = file.read().splitlines()
    return data_list


# name: get_monthly_averages
# param: data_list  - the list that you will process
# brief: get a list of the stock's monthly averages and their corresponding dates
# return: a list


def get_monthly_averages(data_list):
    # INITIAL LINE
    aLine = data_list[1]
    lineItems = aLine.split(',')
    date = lineItems[0]
    data = lineItems[len(lineItems) - 1]
    dateSplit = date.split('/')
    year = dateSplit[2]
    month = dateSplit[0]
    # INITAL LINE

    # MAIN
    oldMonth = month
    sum = 0
    count = 0
    monthly_average_list = []
    monthly_average_list += [['Month', 'Year', 'Average']]
    for i in range(1, len(data_list), 1):
        aLine = data_list[i]
        lineItems = aLine.split(',')
        date = lineItems[0]
        data = lineItems[len(lineItems) - 1]
        dateSplit = date.split('/')
        year = dateSplit[2]
        month = dateSplit[0]

        if month == oldMonth:
            count += 1
            sum += float(data)
            avg = sum / count

        if (month != oldMonth) or i == 1030:
            sum = float(data)
            count = 1
            oldMonth = month
            monthly_average_list += [[oldMonth, year, round(avg, 2)]]

    return monthly_average_list
    # MAIN

# name: print_info
# param: monthly_average_list  - the list that you will process
# brief: print the monthly averages of Google stock
# return: None


def print_info(monthly_average_list):
    for i in range(len(monthly_average_list)):
        print("monthly_average_list[{:^2}]  =  {}".format(str(i), str(monthly_average_list[i])))


print_info(get_monthly_averages(get_data_list('table.csv')))


'''
monthly_average_list[0 ]  =  ['Month', 'Year', 'Average']
monthly_average_list[1 ]  =  ['8', '2008', 437.7]
monthly_average_list[2 ]  =  ['7', '2008', 485.91]
monthly_average_list[3 ]  =  ['6', '2008', 510.03]
monthly_average_list[4 ]  =  ['5', '2008', 556.32]
monthly_average_list[5 ]  =  ['4', '2008', 575.92]
monthly_average_list[6 ]  =  ['3', '2008', 497.58]
monthly_average_list[7 ]  =  ['2', '2008', 440.33]
monthly_average_list[8 ]  =  ['1', '2008', 503.8]
monthly_average_list[9 ]  =  ['12', '2007', 611.81]
monthly_average_list[10]  =  ['11', '2007', 695.4]
monthly_average_list[11]  =  ['10', '2007', 676.37]
monthly_average_list[12]  =  ['9', '2007', 635.39]
monthly_average_list[13]  =  ['8', '2007', 540.43]
monthly_average_list[14]  =  ['7', '2007', 509.83]
monthly_average_list[15]  =  ['6', '2007', 532.48]
monthly_average_list[16]  =  ['5', '2007', 515.02]
monthly_average_list[17]  =  ['4', '2007', 473.01]
monthly_average_list[18]  =  ['3', '2007', 472.5]
monthly_average_list[19]  =  ['2', '2007', 452.91]
monthly_average_list[20]  =  ['1', '2007', 467.22]
monthly_average_list[21]  =  ['12', '2006', 490.58]
monthly_average_list[22]  =  ['11', '2006', 473.5]
monthly_average_list[23]  =  ['10', '2006', 485.63]
monthly_average_list[24]  =  ['9', '2006', 440.53]
monthly_average_list[25]  =  ['8', '2006', 397.06]
monthly_average_list[26]  =  ['7', '2006', 377.09]
monthly_average_list[27]  =  ['6', '2006', 403.53]
monthly_average_list[28]  =  ['5', '2006', 393.59]
monthly_average_list[29]  =  ['4', '2006', 383.8]
monthly_average_list[30]  =  ['3', '2006', 413.78]
monthly_average_list[31]  =  ['2', '2006', 358.87]
monthly_average_list[32]  =  ['1', '2006', 370.0]
monthly_average_list[33]  =  ['12', '2005', 445.71]
monthly_average_list[34]  =  ['11', '2005', 418.95]
monthly_average_list[35]  =  ['10', '2005', 399.14]
monthly_average_list[36]  =  ['9', '2005', 322.47]
monthly_average_list[37]  =  ['8', '2005', 304.24]
monthly_average_list[38]  =  ['7', '2005', 286.92]
monthly_average_list[39]  =  ['6', '2005', 298.21]
monthly_average_list[40]  =  ['5', '2005', 287.55]
monthly_average_list[41]  =  ['4', '2005', 239.71]
monthly_average_list[42]  =  ['3', '2005', 199.21]
monthly_average_list[43]  =  ['2', '2005', 181.16]
monthly_average_list[44]  =  ['1', '2005', 195.01]
monthly_average_list[45]  =  ['12', '2004', 192.85]
monthly_average_list[46]  =  ['11', '2004', 181.77]
monthly_average_list[47]  =  ['10', '2004', 177.5]
monthly_average_list[48]  =  ['9', '2004', 153.23]
monthly_average_list[49]  =  ['8', '2004', 113.23]
monthly_average_list[50]  =  ['8', '2004', 105.26]
'''
