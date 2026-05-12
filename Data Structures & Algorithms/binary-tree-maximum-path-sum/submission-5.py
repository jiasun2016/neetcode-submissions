# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxRoot, _ = self.dfs(root)
        return maxRoot 

    def dfs(self, root):
        if not root:
            return float("-inf"), 0 
        maxleft, leftpath = self.dfs(root.left)
        maxright, rightpath = self.dfs(root.right) 
        maxRoot = max(maxleft, maxright, max(leftpath, 0) + max(rightpath,0) + root.val)
        rootPath = max(leftpath, rightpath, 0) + root.val 
        return maxRoot, rootPath