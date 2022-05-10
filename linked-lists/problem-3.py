# Anneka Curry SPD 2.4

# Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def rotateCounterClockwise(head: ListNode, k: int) -> ListNode:
  if k == 0:
    return head

  origin, point = head, head

  for _ in range(k-1):
    point = point.next

  end = point
  new_head = point.next
  point = point.next
  end.next = None

  while point and point.next:
    point = point.next

  point.next = origin
  return new_head



