# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        if not self.isBalanced(root.left):
            return False 
        if not self.isBalanced(root.right):
            return False 
        return abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1 
        
    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right) 
        return max(left, right) + 1
