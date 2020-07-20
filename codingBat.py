# codingBat.py
# Kyle Garcia
# 7/1/2020
# Python 3.8.3
# Description: Collection of Coding Bat functions

# string_times
def string_times(str, n):
    connect = ''
    for i in range(n):
        connect += str
        return connect


def extra_end(str):
    connect = ''
    for i in range(3):
        connect += str[len(str) - 2:]
    return connect


def make_tags(tag, word):
    tag1 = "<" + tag + ">"
    tag2 = "</" + tag + ">"
    return (tag1 + word + tag2)


def combo_string(a, b):
    if len(a) > len(b):
        return (b + a + b)
    elif len(b) > len(a):
        return (a + b + a)


def count_code(str):
    count = 0
    for i in range(0, len(str) - 3):
        if str[i:i + 2] == 'co' and str[i + 3] == 'e':
            count += 1
  return count


def xyz_there(str):
    count = 0
    count2 = 0
    for i in range(len(str)-2):
        if str[i:i+3] == "xyz":
            count += 1

    for i in range (len(str)-3):
        if str[i:i+4] == ".xyz":
            count2 += 1

    ratio = count - count2
    if ratio > 0:
        return True
    else:
      return False
