# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        preGroup = dummy 
        while True:
            kth = self.getKth(preGroup, k) 
            if not kth:
                break 
            nextGroup = kth.next 
            pre, curr = nextGroup, preGroup.next
            while curr != nextGroup:
                temp = curr.next 
                curr.next = pre
                pre = curr 
                curr = temp 
            temp = preGroup.next 
            preGroup.next = kth 
            preGroup = temp 
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1 
        return curr 
