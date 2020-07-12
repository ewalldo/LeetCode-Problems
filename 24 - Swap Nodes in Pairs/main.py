# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev, node = None, head
        while node and node.next:
            node_next = node.next.next
            node.next.next = node
            
            if prev:
                prev.next = node.next
            else:
                head = node.next
            prev = node
            node.next = node_next
            node = node_next
        return head
