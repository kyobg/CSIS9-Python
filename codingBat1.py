# codingBat1.py
# Kyle Garcia
# 7/9/2020
# Python 3.8.3
# Description: Coding Bat exercises 2.

def centered_average(nums):
    maxm = nums[0]
    minm = nums[0]
    for i in range(len(nums)):
        if nums[i] < minm:
            minm = nums[i]
        if nums[i] > maxm:
            maxm = nums[i]
    average = (sum(nums) - minm - maxm) / (len(nums) - 2)

  return average


def sum13(nums):
    length = len(nums)
    if length == 0:
        return 0
    else:
        for i in range(length-1):
            if nums[i] == 13:
                nums[i] = 0
                nums[i+1] = 0
        if nums[length-1] == 13:
            nums[length-1] = 0
    return sum(nums)


def big_diff(nums):
    maxm = nums[0]
    minm = nums[0]
    for i in range(len(nums)):
        if nums[i] < minm:
            minm = nums[i]
        if nums[i] > maxm:
            maxm = nums[i]
    diff = maxm - minm
    return diff
