# Anneka Curry SPD 2.4

# Given an array of k singly-linked lists, each of whose values are in sorted order, 
# combine all nodes (do not create new nodes) into one singly-linked list with all values in order.


def merge(head1, head2):
  head = None
  head.next = None

  if head1.value < head2.value:
    head = head1
    node1 = head1.next
    node2 = head2

  else:
    head = head2
    node2 = head2.next
    node1 = head1

  node = head

  while node1.next != None and node2.next != None:
    if node1.value < node2.value:
      node.next = node1
      node1 = node1.next
      node = node.next

    else:
      node.next = node2
      node2 = node2.next
      node = node.next

  while node1.next != None:
    node.next = node1
    node1 = node1.next
    node = node.next

  while node2.next != None:
    node.next = node2
    node2 = node2.next
    node = node.next

  return head


def combineLists(arr):
  i = 0
  mergedLists = merge(arr[i], arr[i+1])
  i = 2

  while i <= len(arr) - 1 :
    mergedLists = merge(mergedLists, arr[i])
    i += 1

  return mergedLists