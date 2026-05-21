# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        p1,p2 = l1, l2
        carr = 0
        dummy = ListNode(-1)  
        curr = dummy
        while p1 or p2 or carr:
            if p1: 
                carr += p1.val
                p1 = p1.next 
            if p2:
                carr += p2.val
                p2 = p2.next 
            curr.next = ListNode(carr%10)
            carr = carr//10 
            curr = curr.next
       
        return dummy.next
            
            
        


