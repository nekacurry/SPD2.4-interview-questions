# Anneka Curry SPD 2.4

# Given a binary search tree, reverse the order of its values by modifying the nodes’ links.

def reverseOrder(root):
  if root != None:
    a = reverseOrder(root.left)
    b = reverseOrder(root.right)

    root.left = b
    root.right = a

  return root
