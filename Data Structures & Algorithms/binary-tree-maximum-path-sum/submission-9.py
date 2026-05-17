# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxSum, maxPath = self.dfs(root)
        return maxSum
        
    def dfs(self, root):
        if not root:
            return float("-inf"), 0 
        maxleftSum, leftPath = self.dfs(root.left)
        maxrightSum, rightPath = self.dfs(root.right)
        maxPath = max(leftPath, rightPath, 0) + root.val
        maxSum = max(maxleftSum, maxrightSum, leftPath+ rightPath + root.val)
        return maxSum, max(maxPath, 0) 