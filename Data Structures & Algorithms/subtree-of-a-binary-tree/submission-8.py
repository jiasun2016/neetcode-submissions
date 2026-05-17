# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False 

        if self.isSame(root, subRoot):
            return True 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 


    def isSame(self, p, q):
        if not p and not q:
            return True 
        p1 = [p]
        q1 = [q]
        while p1 and q1:
            n1, n2 = p1.pop(0), q1.pop(0)
            if not n1 and not n2:
                continue 
            if not n1 or not n2:
                return False 
            if n1.val != n2.val:
                return False 
            p1.append(n1.left)
            p1.append(n1.right)
            q1.append(n2.left)
            q1.append(n2.right) 
        return True 
            
    