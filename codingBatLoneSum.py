def lone_sum(a, b, c):
    if a == b and a == c:
        return 0
    elif a == c:
        return b
    elif b == c:
        return a
    if a == b:
        return c
    else:
        return a + b + c


'''
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c

  return sum

'''
