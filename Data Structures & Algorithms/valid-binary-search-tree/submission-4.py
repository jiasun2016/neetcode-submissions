# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        
        return self.dfs(-float('inf'), root, float('inf'))
        
    def dfs(self, leftMax, root, rightMax):
        if not root:
            return True 
        if root.val <= leftMax or root.val >= rightMax:
            return False 
        return self.dfs(leftMax, root.left, root.val) and self.dfs(root.val, root.right, rightMax)