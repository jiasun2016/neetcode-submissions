# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum, path = self.dfs(root)
        return maxSum
    def dfs(self, root):
        if not root:
            return float('-inf'), 0 
        leftMaxSum, left = self.dfs(root.left)
        rightMaxSum, right = self.dfs(root.right)
        maxSum = max(leftMaxSum,rightMaxSum, left + right + root.val)
        path = max(left, right) + root.val 
        return maxSum, max(path, 0)
