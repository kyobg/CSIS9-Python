# codingBat2.py
# Kyle Garcia
# 7/9/2020
# Python 3.8.3
# Description: Coding Bat exercises 3.

def cigar_party(cigars, is_weekend):
    if not is_weekend:
        if cigars < 40:
            return False
    if not is_weekend:
        if cigars > 60:
            return False
    if is_weekend:
        if cigars < 40:
            return False
  return True


def count_evens(nums):
    count = 0
    length = len(nums)
    for i in range(length):
        if nums[i] % 2 == 0:
            count += 1
        else:
            pass
  return count


def has22(nums):
    length = len(nums)
    for i in range(length-1):
        if nums[i] == nums[i + 1] and nums[i] == 2:
            return True
  return False


def sum67(nums):
    sum = 0
    length = len(nums)
    ignore =  False
    for i in range(length):
        if nums[i] == 6:
            ignore = True

        if ignore == False:
            sum += nums[i]

        if nums[i] == 7:
            ignore = False
  return sum
