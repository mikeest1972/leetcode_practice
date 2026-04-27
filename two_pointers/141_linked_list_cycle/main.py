import types
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False
        slow = head
        fast = head.next

        while slow != None and fast != None:
            if slow == fast and slow.val == fast.val and slow.next == fast.next:
                return True
            else:
                slow = slow.next
                fast = fast.next
                if fast == None:
                    return False
                # increment a second time
                fast = fast.next

        return False
        


