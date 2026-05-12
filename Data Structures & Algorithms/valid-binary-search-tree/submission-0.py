# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.dfs(root, float("-inf"), float("inf"))
        
    def dfs(self, root, leftVal, rightVal):
        if not root:
            return True 
        
        if leftVal >= root.val or root.val >= rightVal:
            return False 

        return self.dfs(root.left, leftVal, root.val) and self.dfs(root.right, root.val, rightVal) 

            
