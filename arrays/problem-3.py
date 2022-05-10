# Anneka Curry SPD 2.4 

# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]

def find_largest(a, k):
  arr = []
  for i in range(k):
    largest = max(a)
    arr.append(largest)
    a.remove(largest)
  return arr

a = [5, 1, 3, 6, 8, 2, 4, 7]
k = 3

print(find_largest(a, k))