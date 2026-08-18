# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum, _  = self.dfs(root)
        return maxSum
        

    def dfs(self, root):
        if not root:
            return float('-inf'), 0
        leftMax, leftSum = self.dfs(root.left)
        rightMax, rightSum = self.dfs(root.right)
        pathSum = root.val + max(leftSum, rightSum, 0)
        maxSum = max(leftMax, rightMax,  root.val + leftSum + rightSum) 

        return maxSum, max(pathSum, 0) # 限制了leftSum， rightSum 一定 > = 0

