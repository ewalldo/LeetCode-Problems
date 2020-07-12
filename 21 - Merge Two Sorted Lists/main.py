# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        head = l3
        while (l1 is not None and l2 is not None):
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
            elif l2.val < l1.val:
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next
        while l1 is not None:
            l3.next = ListNode(l1.val)
            l3 = l3.next
            l1 = l1.next
        while l2 is not None:
            l3.next = ListNode(l2.val)
            l3 = l3.next
            l2 = l2.next
        return head.next
