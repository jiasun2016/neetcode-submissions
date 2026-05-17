# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None 
        return self.divide(0, len(lists)-1,lists)
    
    def divide(self, l,r, lists):
        if l == r:
            return lists[l]
        mid = l + (r-l)//2 
        left = self.divide(l, mid, lists)
        right = self.divide(mid+1, r, lists)
        return self.merge(left, right, lists)
            
    def merge(self, l1, l2, lists):
        temp = ListNode(-1,None)
        curr = temp
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1 
                l1 = l1.next
            else:
                curr.next = l2 
                l2 = l2.next 
            curr = curr.next 
        if l1:
            curr.next = l1 
        if l2:
            curr.next = l2 
        return temp.next 


