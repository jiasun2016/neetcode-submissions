# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD, maxp = self.dfs(root)
        return maxD
    def dfs(self, root):
        if not root:
            return 0, 0
        leftmaxD, leftmaxP = self.dfs(root.left)
        rightmaxD, rightmaxP = self.dfs(root.right) 
        maxD = max(leftmaxD, rightmaxD, leftmaxP + rightmaxP )
        return maxD, max(leftmaxP, rightmaxP) + 1