# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 
        
    # def helper(self, node, h):
    #     if not node:
    #         return h 
    #     return max(self.helper(node.left, h+1), self.helper(node.right, h+1)) 