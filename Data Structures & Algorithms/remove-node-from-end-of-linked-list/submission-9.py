# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        fast= slow = dummy 
        while n>0:
            if fast:
                fast = fast.next 
            else:
                return None 
            n -=1 
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next 
        return dummy.next 