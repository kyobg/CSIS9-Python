# p43_dataMining.py
# Kyle Garcia
# 7/19/2020
# Python 3.8.3
# Description: Program that calculates the average of each month of every year.

# name: get_data_list
# param: FILE_NAME  - the file's name you saved for the stock's prices
# brief: get a list of the stock's records' lists
# return: a list of lists

# Reads the file and breaks it up into a large data list
def get_data_list(FILE_NAME):
    file = open(FILE_NAME)
    data_list = file.read().splitlines()
    for i in range(1, len(data_list)):
        data_list[i] = data_list[i].split(',')
    # print(data_list)
    return data_list

# name: get_monthly_averages
# param: data_list  - the list that you will process
# brief: get a list of the stock's monthly averages and their corresponding dates
# return: a list


'''
======================
    list position:
======================
    1) Date
    2) open
    3) high
    4) low
    5) close
    6) volume
    7) adj close
'''


def get_monthly_averages(data_list):
    '''for i in range(1, len(data_list)):  # Separates the dates by '/'
        data_list[i][0] = data_list[i][0].split('/')  # Separates the dates by '/'
        #         ^from base list      ^from list in base list

        # Now I need to find a way to average the open/closes/etc
        #  ========================================================================== START OF AVERAGE
        sum = 0
        for j in range(1, len(data_list[i]) - 2):
            sub_list = data_list[i]
            sub_list[j] = float(sub_list[j])
            sum += sub_list[j]
            avg = sum / (len(data_list[i]) - 3)
            avg = round(avg, 2)
        print(data_list[i][0], avg)
    # ================================================== END OF AVERAGE
    # Returns
    '''  # Scrapped, this calculates the average of each day, not month
'''    monthAverage = []
    count = 0
    for i in range(1, len(data_list)):
        data_list[i][0] = data_list[i][0].split('/')  # turn dates into a list

    for j in range(1, len(data_list) - 1):
        if data_list[j][0][0] == data_list[j + 1][0][0]:  # if months are the same...
            count += 1
    print(count)


'''

    monthly_average_list_header = ['Month', 'Year', 'Average']

    print(data_list)
    print(monthly_average_list_header)

    return monthly_average_list


# name: print_info
# param: monthly_average_list  - the list that you will process
# brief: print the monthly averages of Google stock
# return: None


def print_info(monthly_average_list):

    pass
    #  show monthly averages of Google stock

#  1) call get_data_list(FILE_NAME) function to get the data list.
#  Return into variable data_list

#  2) call get_monthly_averages(data_list) function with variable data_list from above as argument.
#  Return into variable monthly_average_list

#  3) call print_info(monthly_average_list) function with variable monthly_average_list from above as argument.
#  Show the monthly_average_list as shown in the sample run below

get_monthly_averages(get_data_list('table.csv'))
