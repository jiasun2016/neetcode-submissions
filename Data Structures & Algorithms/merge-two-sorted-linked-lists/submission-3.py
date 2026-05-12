# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = list1, list2 
        dummy = ListNode(-1)
        curr = dummy
        while a and b:
            if a.val > b.val:
                curr.next = b 
                b = b.next 
            else:
                curr.next = a 
                a = a.next 
            curr = curr.next 
        
        curr.next = a or b
        return dummy.next 
        

