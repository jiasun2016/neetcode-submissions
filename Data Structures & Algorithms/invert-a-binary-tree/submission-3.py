# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 
        stack = [root]
        while stack:
            p = stack.pop(0)
            if p.right:
                stack.append(p.right) 
            if p.left:
                stack.append(p.left) 
            p.right, p.left  = p.left, p.right
        return root
