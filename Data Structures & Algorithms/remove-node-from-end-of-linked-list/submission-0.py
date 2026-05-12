# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        pre = head
        pos = dummy
        while n> 0:
            if not pre: 
                return None 
            pre = pre.next
            n -= 1
        
        while pre:
            pre = pre.next 
            pos = pos.next 
        pos.next = pos.next.next 
        return dummy.next

