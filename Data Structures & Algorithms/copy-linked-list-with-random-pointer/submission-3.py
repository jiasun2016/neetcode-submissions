"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copys = {}
        if not head:
            return 
        curr = head
        while curr:
            copys[curr] = Node(curr.val) 
            curr = curr.next 
        curr = head 
        while curr:
            copy = copys[curr]
            copy.next = copys.get(curr.next)
            copy.random = copys.get(curr.random) 
            curr = curr.next 
        return copys[head]
        
