# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum, single = self.dfs(root) 
        return maxSum
    def dfs(self, root):
        if not root:
            return float("-inf"), 0 

        leftSum, leftSingle = self.dfs(root.left)
        rightSum, rightSingle = self.dfs(root.right) 

        maxSum = max(leftSum, rightSum, root.val + leftSingle + rightSingle)
        singleSum = max(leftSingle + root.val, rightSingle + root.val, 0, root.val) # based on dfs, signle path mast >= 0
        return maxSum, singleSum
    