# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        for i in range(k):
            if not stack:
                return None 
            node = stack.pop()
            if node.right:
                node = node.right 
                while node:
                    stack.append(node)
                    node = node.left
            
        return stack[-1].val