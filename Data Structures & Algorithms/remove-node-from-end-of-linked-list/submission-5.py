# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        if not head:
            return 
        slow, fast = dummy, dummy 
        for i in range(n):
                if not fast:
                    return 
                fast = fast.next 
        while fast.next:
            fast = fast.next 
            slow = slow.next 
        slow.next = slow.next.next 
        return dummy.next
