# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.swap(head)

    def swap(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        temp = head
        head = head.next
        temp.next = self.swap(head.next)
        head.next = temp
        return head