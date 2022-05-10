# Anneka Curry SPD 2.4

# Given two arrays a and b of numbers and a target value t,
# find a number from each array whose sum is closest to t.

# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  
# t=20  ⇒  [13, 6] or [4, 17] or [5, 14]


def find_closest(a, b, t):
  a_sort = sorted(a)
  b_sort = sorted(b)

  x, y, = 0, len(b_sort) - 1
  left, right = 0, len(b_sort) - 1

  while left < len(a_sort) and right >= 0:
    if abs(a_sort[left] + b_sort[right] - t) < abs(a_sort[x] + b_sort[y] - t):
      x = left
      y = right

    if a_sort[left] + b_sort[right] < t:
      left += 1

    elif a_sort[left] + b_sort[right] < t:
      right -= 1

    else:
      left += 1
      right -= 1

  return [a_sort[x], b_sort[y]]

a = [9, 13, 1, 8, 12, 4, 0, 5]
b = [3, 17, 4, 14, 6]
t = 20

print(find_closest(a, b, t))