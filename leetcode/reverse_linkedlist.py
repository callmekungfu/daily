# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self): 
        self.head = None

    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        self.reverse(head, None)
        return self.head
    
    def reverse(self, curr, prev):
        if curr.next == None:
            self.head = curr
            curr.next = prev 
            return
        next = curr.next
        curr.next = prev
        self.reverse(next, curr)