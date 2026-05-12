# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float("-inf"), float("inf"))
        
    def isValid(self, root, leftMax, rightMax):
        if not root:
            return True 
        if leftMax >= root.val or rightMax <= root.val:
            return False 
        return  self.isValid(root.left, leftMax, root.val) and self.isValid(root.right,root.val, rightMax)
    