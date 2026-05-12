# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        maxH, isBalance = self.getDepth(root)
        return isBalance
        
    def getDepth(self, root):
        if not root:
            return 0, True
        left, leftB = self.getDepth(root.left)
        right, rightB = self.getDepth(root.right) 
        return max(left, right) + 1, abs(left -right ) <= 1 and leftB and rightB
