# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        queue = collections.deque([(root,float("-inf"), float("inf"))]) 
        while queue:
            node, leftVal, rightVal = queue.popleft()
            if node.val <= leftVal or node.val >= rightVal:
                return False 
            if node.left:
                queue.append((node.left, leftVal, node.val))
            
            if node.right:
                queue.append((node.right, node.val, rightVal)) 
        return True