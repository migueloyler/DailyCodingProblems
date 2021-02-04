# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False 
        if head == head.next:
            return True

        turtle = head.next
        hare = head.next.next
        while (True):
            if turtle.next == None:
                return False
            if hare.next == None:
                return False
            if hare.next.next == None:
                return False
            if turtle == hare:
                return True
            turtle = turtle.next
            hare = hare.next.next
        return False
