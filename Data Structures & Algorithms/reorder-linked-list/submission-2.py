# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head 
        fast, slow = head, head 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
        second = slow.next 
        slow.next = None 
        temp2 = second 
        prev = None
        while temp2:
            nxt = temp2.next 
            temp2.next = prev 
            prev = temp2 
            temp2 = nxt 
        first, second = head, prev 
        while second:
            nxt1, nxt2 = first.next, second.next 
            first.next = second 
            first = nxt1
            second.next = nxt1 
            second = nxt2  

            
        
