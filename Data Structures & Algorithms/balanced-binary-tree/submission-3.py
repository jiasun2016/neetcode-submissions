# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isB, maxH = self.dfs(root)
        return isB
        
    def dfs(self, root):
        if not root:
            return True, 0 
        leftB, leftH = self.dfs(root.left)
        rightB, rightH = self.dfs(root.right)
        return leftB and rightB and abs(leftH - rightH) <= 1, max(leftH, rightH)+1
        