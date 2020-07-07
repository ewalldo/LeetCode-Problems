# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_head = ListNode(0)
        carry = 0
        p = l1
        q = l2
        curr = result_head
        
        while p != None or q != None:
            if p != None:
                x = p.val
            else:
                x = 0
                
            if q != None:
                y = q.val
            else:
                y = 0
                
            sum = carry + x + y
            carry = int(sum / 10)
            
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
            if (p != None):
                p = p.next
            if (q != None):
                q = q.next
                
        if carry > 0:
            curr.next = ListNode(carry)
            
        return result_head.next
