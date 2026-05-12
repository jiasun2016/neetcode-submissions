# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxhight, diameter = self.dfs(root)
        return diameter

    def dfs(self, root):
        if not root:
            return 0, 0
        left,leftDiameter = self.dfs(root.left) 
        right, rightDimater = self.dfs(root.right) 

        diameter = max(leftDiameter, rightDimater, left + right) 
        return max(left, right)+1, diameter
    
        