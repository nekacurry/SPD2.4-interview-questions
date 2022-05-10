# Given a sorted array of strings, write a recursive function 
# to find the index of the first and last occurrence of a target string. 
# If the target string is not found in the array, report that.

# Example input:
# instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, 
#                Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, 
#                Dan, Dani, Dani, Jess, Meredith, Milad, Milad, 
#                Mitchell, Mitchell, Mitchell, Mitchell]

# Example execution:  
# find_indexes(instructors, 'Braus')  ⇒  (7, 10)

# Anneka Curry SPD 2.4

def find_indexes(arr, target):
  indexes = []

  def r_search(index):

    if index >= len(arr):
      return

    elif arr[index] == target and len(indexes) == 0:
      indexes.append(index)

    elif arr[index] != target and len(indexes) == 1:
      indexes.append(index - 1)

    r_search(index + 1)

  r_search(0)
  return indexes


instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 
                'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan','Dan',
                'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 
                'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']

print(find_indexes(instructors, 'Braus'))


