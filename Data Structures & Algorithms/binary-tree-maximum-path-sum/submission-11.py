# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum, p = self.dfs(root)
        return maxSum
    def dfs(self, root):
        if not root:
            return float('-inf'), 0 
        leftMax, leftPath = self.dfs(root.left)
        rightMax, rightPath = self.dfs(root.right) 
        path = max(leftPath, rightPath) + root.val
        maxSum = max(leftMax, rightMax, leftPath+ rightPath + root.val)
        return maxSum, max(0, path)