class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_two_lists(l1, l2):
    head = ListNode(0) # Create Dummy Node
    temp_1 = l1
    temp_2 = l2
    temp_head = head

    while temp_1 != None or temp_2 != None:
        if (temp_1.val <= temp_2.val):
            temp_head.next = temp_1
            temp_1 = temp_1.next
        else:
            temp_head.next = temp_2
            temp_2 = temp_2.next
        temp_head = temp_head.next

    if temp_1 == None:
        temp_head.next = temp_2
    if temp_2 == None:
        temp_head.next = temp_1
    
    return head.next